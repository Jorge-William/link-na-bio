# link-na-bio

SaaS de **perfil e site profissional** (bio + institucional): editor, publicação na edge, **assinatura recorrente**. Domínio da plataforma: **[linkk.ae](https://linkk.ae)**. Infra fixa: **Cloudflare**. Stack do app: **flexível**.

## Status

**F0 em andamento** — monorepo, schema SQL, Workers `www` / `app` / `sites` / `publish`, CI.

```bash
npm install
npm run build -w @linknabio/shared
npm test
npm run dev:www   # landing
npm run dev:app   # API shell
```

Guia: **[docs/desenvolvimento.md](docs/desenvolvimento.md)**

## Começar aqui (produto)

1. **[docs/produto-e-receita.md](docs/produto-e-receita.md)** — MRR, planos, CF fixo vs flexível
2. **[docs/casos-de-uso.md](docs/casos-de-uso.md)** — 95 casos de uso
3. **[docs/plano-construcao.md](docs/plano-construcao.md)** — fases F0–F6

## Código

| Path | Conteúdo |
|---|---|
| `apps/www` | Landing (Assets) |
| `apps/app` | Dashboard + API |
| `apps/sites` | Origin público Host → R2 |
| `apps/publish` | Queue consumer → HTML |
| `packages/shared` | Planos, tipos, parse Host |
| `schema/d1` | Migrations SQL |
| `infra/terraform` | Plataforma CF |

## Docs de referência

| Doc | Conteúdo |
|---|---|
| [desenvolvimento.md](docs/desenvolvimento.md) | Como rodar local |
| [analytics.md](docs/analytics.md) | Analytics Pro |
| [tenants-e-dominios.md](docs/tenants-e-dominios.md) | Três origens, DNS |
| [signup-e-psp.md](docs/signup-e-psp.md) | PSP porteiro |
| [freemium.md](docs/freemium.md) | Free como canal |
| [cloudflare-infra.md](docs/cloudflare-infra.md) | Contrato de infra |
| [cloudflare-terraform.md](docs/cloudflare-terraform.md) | Terraform × Wrangler |
| [concorrente-appsha.md](docs/concorrente-appsha.md) | Benchmark Appsha |
| [design-appsha.md](docs/design-appsha.md) | UI de referência |
