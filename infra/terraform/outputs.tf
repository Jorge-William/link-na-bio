output "zone_id" {
  value       = data.cloudflare_zone.platform.id
  description = "Zone ID — custom domains e SaaS."
}

output "r2_bucket_name" {
  value       = module.platform.r2_bucket_name
  description = "Binding R2 nos workers www/app/sites/hugo."
}

output "d1_database_id" {
  value       = module.platform.d1_database_id
  description = "database_id no wrangler.toml."
}

output "d1_database_name" {
  value       = module.platform.d1_database_name
}

output "kv_namespace_id" {
  value       = module.platform.kv_namespace_id
  description = "KV host-map — app grava, sites lê."
}

output "publish_queue_name" {
  value       = module.platform.publish_queue_name
  description = "Queue entre app (producer) e hugo (consumer)."
}

output "publish_queue_id" {
  value       = module.platform.publish_queue_id
}

output "dns_records" {
  value = {
    www   = "www.${var.zone_name}"
    app   = "app.${var.zone_name}"
    sites = "*.${local.sites_zone}"
  }
}

locals {
  sites_zone = "sites.${var.zone_name}"
}
