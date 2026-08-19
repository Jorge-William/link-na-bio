data "cloudflare_zone" "platform" {
  name = var.zone_name
}

module "platform" {
  source = "./modules/platform"

  account_id  = var.account_id
  environment = var.environment
  r2_location = var.r2_location
}

module "dns" {
  source = "./modules/dns"

  zone_id     = data.cloudflare_zone.platform.id
  zone_name   = var.zone_name
  environment = var.environment

  www_target   = var.worker_www_target
  app_target   = var.worker_app_target
  sites_target = var.worker_sites_target
}

module "saas" {
  count  = var.enable_saas_fallback ? 1 : 0
  source = "./modules/saas"

  zone_id  = data.cloudflare_zone.platform.id
  zone_name = var.zone_name
}
