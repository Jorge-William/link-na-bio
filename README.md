# link-na-bio

SaaS de páginas de **link na bio** e institucionais/portfólio: editor no dashboard, publicação Hugo estática, recorrência na bio.

## Infra: tenants e domínios

O fluxo de signup, a distribuição de tenants e o desenho de DNS estão em:

**[docs/tenants-e-dominios.md](docs/tenants-e-dominios.md)**

Lá estão as origens (`www` / `app` / `sites`), os diagramas Mermaid (checkout → magic link → publish, lookup por Host, onboard, ciclo da assinatura) e o que não misturar — cookie de dashboard no host público, um site Hostinger por cliente, etc.
