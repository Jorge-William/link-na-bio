# Desenvolvimento — F0

## Pré-requisitos

- Node 20+
- Conta Cloudflare (para deploy; local funciona sem)

```bash
npm install
npm run build -w @linknabio/shared
npm test
```

## Apps

| Pacote | Comando | Papel |
|---|---|---|
| `@linknabio/www` | `npm run dev:www` | Landing estática + `/health` |
| `@linknabio/app` | `npm run dev:app` | API/dashboard shell |
| `@linknabio/sites` | `npm run dev:sites` | Origin público (Host → R2) |
| `@linknabio/publish` | `npm run dev:publish` | Consumer da fila publish |
| `@linknabio/shared` | `npm test -w @linknabio/shared` | Planos, host parse, tipos |

## Schema

```bash
# Após criar D1 real e preencher database_id nos wrangler.toml:
npx wrangler d1 migrations apply linknabio-prod --local
```

SQL em `schema/d1/0001_init.sql`.

## Bindings placeholder

Os `wrangler.toml` usam IDs dummy (`0000…`). Troque pelos outputs do Terraform (`infra/terraform`) antes do deploy remoto.

```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
# terraform apply → copiar r2_bucket_name, d1_database_id, kv_namespace_id
```

## Próximo (F1)

1. Magic link + sessão
2. Checkout PSP + webhook
3. Onboard slug → enqueue publish
4. Editor mínimo (links + WhatsApp)

Ver [docs/plano-construcao.md](../docs/plano-construcao.md).
