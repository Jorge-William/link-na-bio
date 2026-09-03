import type { PageModel, PublishJob } from "@linknabio/shared";

export interface Env {
  DB: D1Database;
  SITES: R2Bucket;
  HOST_MAP: KVNamespace;
  SERVICE_NAME: string;
}

/**
 * Consumer da fila publish (UC-41).
 * F0: aceita job e grava HTML mínimo a partir do page_model.
 * F1+: renderer completo (templates / SSG).
 */
export default {
  async fetch(): Promise<Response> {
    return Response.json({
      ok: true,
      service: "publish",
      hint: "Este Worker consome a Queue; não é HTTP origin.",
    });
  },

  async queue(
    batch: MessageBatch<PublishJob>,
    env: Env,
  ): Promise<void> {
    for (const msg of batch.messages) {
      try {
        await handlePublish(msg.body, env);
        msg.ack();
      } catch (err) {
        console.error("publish failed", msg.body, err);
        msg.retry();
      }
    }
  },
} satisfies ExportedHandler<Env, PublishJob>;

async function handlePublish(job: PublishJob, env: Env): Promise<void> {
  const row = await env.DB.prepare(
    `SELECT t.slug, t.plan, t.public_status, p.draft_json
     FROM tenants t
     LEFT JOIN page_models p ON p.tenant_id = t.id
     WHERE t.id = ?`,
  )
    .bind(job.tenantId)
    .first<{
      slug: string | null;
      plan: string;
      public_status: string;
      draft_json: string | null;
    }>();

  if (!row?.slug) {
    throw new Error(`tenant ${job.tenantId} sem slug`);
  }

  const model = JSON.parse(row.draft_json || "{}") as PageModel;
  const html = renderBioHtml(model, row.plan === "free");

  const prefix = `sites/${job.tenantId}/current`;
  await env.SITES.put(`${prefix}/index.html`, html, {
    httpMetadata: { contentType: "text/html; charset=utf-8" },
  });

  const mapValue = JSON.stringify({
    tenantId: job.tenantId,
    status: "live",
    plan: row.plan,
    prefix,
  });

  await env.HOST_MAP.put(`slug:${row.slug}`, mapValue, {
    expirationTtl: 86400 * 7,
  });

  await env.DB.prepare(
    `UPDATE tenants
     SET current_rev = ?, public_status = 'live',
         last_published_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now'),
         updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
     WHERE id = ?`,
  )
    .bind(job.rev, job.tenantId)
    .run();

  await env.DB.prepare(
    `UPDATE page_models SET published_json = draft_json,
       updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
     WHERE tenant_id = ?`,
  )
    .bind(job.tenantId)
    .run();
}

function renderBioHtml(model: PageModel, showSeal: boolean): string {
  const name = escapeHtml(model.profile?.name ?? "Sem nome");
  const bio = escapeHtml(model.profile?.bio ?? "");
  const blocks = (model.blocks ?? [])
    .map((b) => {
      if (b.type === "link") {
        const title = escapeHtml(String(b.title ?? "Link"));
        const url = escapeHtml(String(b.url ?? "#"));
        return `<a class="btn" href="${url}" rel="noopener">${title}</a>`;
      }
      if (b.type === "whatsapp") {
        const title = escapeHtml(String(b.title ?? "WhatsApp"));
        const phone = String(b.phone ?? "").replace(/\D/g, "");
        const msg = encodeURIComponent(String(b.message ?? ""));
        const href = `https://wa.me/${phone}${msg ? `?text=${msg}` : ""}`;
        return `<a class="btn wa" href="${href}" rel="noopener">${title}</a>`;
      }
      return "";
    })
    .join("\n");

  const seal = showSeal
    ? `<footer><a href="https://www.linkk.ae">Feito com linkk.ae</a></footer>`
    : "";

  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>${name}</title>
<style>
body{margin:0;font-family:system-ui,sans-serif;background:#0f172a;color:#fff;min-height:100vh}
main{max-width:420px;margin:0 auto;padding:2.5rem 1.25rem;text-align:center}
.avatar{width:88px;height:88px;border-radius:50%;background:#334155;margin:0 auto 1rem}
h1{font-size:1.35rem;margin:0 0 .5rem}
.bio{color:#94a3b8;margin:0 0 1.5rem}
.btn{display:block;padding:.9rem 1rem;margin:.55rem 0;border-radius:10px;background:#fff;color:#0f172a;text-decoration:none;font-weight:600}
.btn.wa{background:#25d366;color:#fff}
footer{margin-top:2rem;font-size:.75rem}
footer a{color:#64748b}
</style>
</head>
<body>
<main>
  <div class="avatar"></div>
  <h1>${name}</h1>
  ${bio ? `<p class="bio">${bio}</p>` : ""}
  ${blocks}
  ${seal}
</main>
</body>
</html>`;
}

function escapeHtml(s: string): string {
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}
