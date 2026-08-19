terraform {
  required_version = ">= 1.5.0"

  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 5.19"
    }
  }

  # backend "s3" { ... }  # ver README — R2 como state store
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}
