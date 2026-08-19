# Terraform — link-na-bio

Plataforma Cloudflare fixa. Workers deployam via Wrangler usando os `outputs`.

## Pré-requisitos

- Terraform >= 1.5
- Token Cloudflare (Account + Zone)
- Zona já adicionada na Cloudflare (`var.zone_name`)

## Uso

```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
# editar account_id, zone_name

terraform init
terraform plan
terraform apply
```

Depois do apply, copie os outputs para os `wrangler.toml` dos workers:

```toml
# wrangler.toml (app)
[[d1_databases]]
binding = "DB"
database_name = "linknabio-prod"   # output d1_database_name
database_id = "<output d1_database_id>"

[[kv_namespaces]]
binding = "HOST_MAP"
id = "<output kv_namespace_id>"

[[queues.producers]]
binding = "PUBLISH"
queue = "linknabio-publish-prod"

[[r2_buckets]]
binding = "SITES"
bucket_name = "<output r2_bucket_name>"
```

## Módulos

| Módulo | Cria |
|---|---|
| `platform` | R2, D1, KV, Queue |
| `dns` | `www`, `app`, `*.sites`, dummy A para fallback |
| `saas` | `custom_hostname_fallback_origin` (habilitar quando for v2) |

## Backend (recomendado)

Descomente em `versions.tf` e crie bucket `linknabio-tfstate`:

```hcl
terraform {
  backend "s3" {
    bucket = "linknabio-tfstate"
    key    = "prod/terraform.tfstate"
    endpoints = { s3 = "https://<account_id>.r2.cloudflarestorage.com" }
    region                      = "auto"
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_region_validation      = true
  }
}
```
