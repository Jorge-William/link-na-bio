variable "cloudflare_api_token" {
  type        = string
  sensitive   = true
  description = "Token com permissão Account (Workers, R2, D1, KV, Queues) + Zone DNS/SSL."
}

variable "account_id" {
  type        = string
  description = "Cloudflare account ID."
}

variable "zone_name" {
  type        = string
  description = "Domínio raiz da plataforma, ex: linknabio.com."
}

variable "environment" {
  type        = string
  default     = "prod"
  description = "Sufixo nos nomes de recursos (prod, staging)."
}

variable "r2_location" {
  type        = string
  default     = "wnam"
  description = "Região do bucket R2: wnam, enam, weur, eeur, apac, oc."
}

variable "enable_saas_fallback" {
  type        = bool
  default     = false
  description = "true quando for ligar Custom Hostname (domínio do cliente)."
}

variable "worker_www_target" {
  type        = string
  description = "CNAME de www — hostname do worker após wrangler deploy (custom domain ou workers.dev)."
}

variable "worker_app_target" {
  type        = string
  description = "CNAME de app."
}

variable "worker_sites_target" {
  type        = string
  description = "CNAME de *.sites e sites."
}
