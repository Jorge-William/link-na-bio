-- F0 schema — D1 / SQLite-compatible. tenant_id em toda linha de negócio.

PRAGMA foreign_keys = ON;

CREATE TABLE users (
  id TEXT PRIMARY KEY NOT NULL,
  email TEXT NOT NULL COLLATE NOCASE,
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  deleted_at TEXT
);

CREATE UNIQUE INDEX users_email_uq ON users (email) WHERE deleted_at IS NULL;

CREATE TABLE tenants (
  id TEXT PRIMARY KEY NOT NULL,
  owner_user_id TEXT NOT NULL REFERENCES users (id),
  slug TEXT COLLATE NOCASE,
  kind TEXT NOT NULL DEFAULT 'bio' CHECK (kind IN ('bio', 'institutional', 'portfolio')),
  plan TEXT NOT NULL DEFAULT 'free' CHECK (plan IN ('free', 'pro', 'business', 'agency')),
  public_status TEXT NOT NULL DEFAULT 'draft'
    CHECK (public_status IN ('draft', 'live', 'paused_billing', 'paused_inactivity')),
  theme TEXT NOT NULL DEFAULT 'default',
  current_rev INTEGER NOT NULL DEFAULT 0,
  last_published_at TEXT,
  last_visit_at TEXT,
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE UNIQUE INDEX tenants_slug_uq ON tenants (slug) WHERE slug IS NOT NULL;
CREATE INDEX tenants_owner_idx ON tenants (owner_user_id);

CREATE TABLE subscriptions (
  id TEXT PRIMARY KEY NOT NULL,
  user_id TEXT NOT NULL REFERENCES users (id),
  tenant_id TEXT NOT NULL REFERENCES tenants (id),
  plan TEXT NOT NULL CHECK (plan IN ('free', 'pro', 'business', 'agency')),
  status TEXT NOT NULL DEFAULT 'active'
    CHECK (status IN ('active', 'trialing', 'past_due', 'paused', 'canceled')),
  psp TEXT,
  psp_customer_id TEXT,
  psp_subscription_id TEXT,
  current_period_end TEXT,
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE INDEX subscriptions_tenant_idx ON subscriptions (tenant_id);
CREATE INDEX subscriptions_psp_sub_idx ON subscriptions (psp_subscription_id);

CREATE TABLE page_models (
  tenant_id TEXT PRIMARY KEY NOT NULL REFERENCES tenants (id) ON DELETE CASCADE,
  draft_json TEXT NOT NULL DEFAULT '{}',
  published_json TEXT,
  updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE TABLE custom_domains (
  id TEXT PRIMARY KEY NOT NULL,
  tenant_id TEXT NOT NULL REFERENCES tenants (id) ON DELETE CASCADE,
  hostname TEXT NOT NULL COLLATE NOCASE,
  cf_hostname_id TEXT,
  status TEXT NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'active', 'failed', 'removed')),
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE UNIQUE INDEX custom_domains_hostname_uq ON custom_domains (hostname)
  WHERE status != 'removed';
CREATE INDEX custom_domains_tenant_idx ON custom_domains (tenant_id);

CREATE TABLE magic_links (
  id TEXT PRIMARY KEY NOT NULL,
  user_id TEXT NOT NULL REFERENCES users (id) ON DELETE CASCADE,
  token_hash TEXT NOT NULL,
  expires_at TEXT NOT NULL,
  used_at TEXT,
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE INDEX magic_links_token_idx ON magic_links (token_hash);

CREATE TABLE webhook_events (
  id TEXT PRIMARY KEY NOT NULL,
  psp TEXT NOT NULL,
  event_id TEXT NOT NULL,
  received_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE UNIQUE INDEX webhook_events_uq ON webhook_events (psp, event_id);

CREATE TABLE publish_jobs (
  id TEXT PRIMARY KEY NOT NULL,
  tenant_id TEXT NOT NULL REFERENCES tenants (id),
  rev INTEGER NOT NULL,
  status TEXT NOT NULL DEFAULT 'queued'
    CHECK (status IN ('queued', 'building', 'live', 'failed')),
  error TEXT,
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  finished_at TEXT
);

CREATE INDEX publish_jobs_tenant_idx ON publish_jobs (tenant_id, created_at DESC);
