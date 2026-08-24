# link-na-bio

SaaS de páginas de **link na bio** e institucionais/portfólio: editor no dashboard, publicação Hugo estática, recorrência na bio.

## Docs

- **[docs/cloudflare-infra.md](docs/cloudflare-infra.md)** — Cloudflare como infra: três Workers, R2, D1, Queue + Container Hugo, Custom Hostname.
- **[docs/cloudflare-plano-pago.md](docs/cloudflare-plano-pago.md)** — Workers Paid (US$ 5): cabe?, cada nó do diagrama, o que ignorar na página de preço.
- **[docs/cloudflare-terraform.md](docs/cloudflare-terraform.md)** — Terraform × Wrangler: o que vai no state, o que fica no CI.
- **[docs/signup-e-psp.md](docs/signup-e-psp.md)** — PSP como porteiro, signup pago/free, quem cria a conta.
- **[docs/concorrente-appsha.md](docs/concorrente-appsha.md)** — Appsha esmiuçado: features, o que copiar (P0–P2) e o que não entrar.
- **[docs/design-appsha.md](docs/design-appsha.md)** — UI Appsha (cores, perfil, editor, signup): o que roubar pro nosso app.
- **[infra/terraform/](infra/terraform/)** — módulos `platform`, `dns`, `saas` (R2, D1, KV, Queue, DNS).
- **[docs/tenants-e-dominios.md](docs/tenants-e-dominios.md)** — origens (`www` / `app` / `sites`), checkout → magic link → publish, lookup por Host, onboard, ciclo da assinatura.
- **[docs/freemium.md](docs/freemium.md)** — plano free, selo no rodapé (não marca d’água), o que converte para premium, limites e pausa por inatividade.
