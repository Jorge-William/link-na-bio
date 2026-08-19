locals {
  prefix = "linknabio"
}

resource "cloudflare_r2_bucket" "sites" {
  account_id    = var.account_id
  name          = "${local.prefix}-sites-${var.environment}"
  location      = var.r2_location
  storage_class = "Standard"
}

resource "cloudflare_d1_database" "main" {
  account_id            = var.account_id
  name                  = "${local.prefix}-${var.environment}"
  primary_location_hint = var.r2_location
}

resource "cloudflare_workers_kv_namespace" "host_map" {
  account_id = var.account_id
  title      = "${local.prefix}-host-map-${var.environment}"
}

resource "cloudflare_queue" "publish" {
  account_id = var.account_id
  queue_name = "${local.prefix}-publish-${var.environment}"
}
