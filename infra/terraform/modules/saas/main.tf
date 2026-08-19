# Habilitar Cloudflare for SaaS na zona antes do apply.
# Fallback origin aponta para sites.{zone} — o Worker sites atende via route */*.

resource "cloudflare_custom_hostname_fallback_origin" "sites" {
  zone_id = var.zone_id
  origin  = "sites.${var.zone_name}"
}
