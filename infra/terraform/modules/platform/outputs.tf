output "r2_bucket_name" {
  value = cloudflare_r2_bucket.sites.name
}

output "d1_database_id" {
  value = cloudflare_d1_database.main.id
}

output "d1_database_name" {
  value = cloudflare_d1_database.main.name
}

output "kv_namespace_id" {
  value = cloudflare_workers_kv_namespace.host_map.id
}

output "publish_queue_name" {
  value = cloudflare_queue.publish.queue_name
}

output "publish_queue_id" {
  value = cloudflare_queue.publish.queue_id
}
