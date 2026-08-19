variable "zone_id" {
  type = string
}

variable "zone_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "www_target" {
  type        = string
  description = "CNAME target do worker www (custom domain ou workers.dev)."
}

variable "app_target" {
  type = string
}

variable "sites_target" {
  type = string
}
