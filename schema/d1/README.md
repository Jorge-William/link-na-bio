# Schema SQL

Migrations em ordem numérica (`0001_…`, `0002_…`). Compatível com **D1** (SQLite).

```bash
# Com conta Cloudflare configurada:
npx wrangler d1 migrations apply linknabio-prod --remote
npx wrangler d1 migrations apply linknabio-prod --local
```

O Worker `app` referencia o banco via binding `DB` (ver `apps/app/wrangler.toml`).
