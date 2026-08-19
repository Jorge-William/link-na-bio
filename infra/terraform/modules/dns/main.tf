locals {
  sites_zone = "sites.${var.zone_name}"
}

# Dummy A exigido pelo fallback origin SaaS (Worker é o origin real).
resource "cloudflare_dns_record" "fallback_origin" {
  zone_id = var.zone_id
  name    = "fallback"
  type    = "A"
  content = "192.0.2.0"
  proxied = true
  comment = "Cloudflare for SaaS fallback origin (dummy)"
}

resource "cloudflare_dns_record" "www" {
  zone_id = var.zone_id
  name    = "www"
  type    = "CNAME"
  content = var.www_target
  proxied = true
  comment = "Marketing — worker www"
}

resource "cloudflare_dns_record" "app" {
  zone_id = var.zone_id
  name    = "app"
  type    = "CNAME"
  content = var.app_target
  proxied = true
  comment = "Dashboard — worker app"
}

# Wildcard só no subdomínio sites — não no apex.
resource "cloudflare_dns_record" "sites_wildcard" {
  zone_id = var.zone_id
  name    = "*.sites"
  type    = "CNAME"
  content = var.sites_target
  proxied = true
  comment = "Bios publicadas — worker sites"
}

resource "cloudflare_dns_record" "sites_zone" {
  zone_id = var.zone_id
  name    = local.sites_zone
  type    = "CNAME"
  content = var.sites_target
  proxied = true
  comment = "Fallback origin hostname para SaaS"
}
