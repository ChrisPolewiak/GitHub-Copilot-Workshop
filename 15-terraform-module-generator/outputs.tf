output "storage_account_id" {
  value       = azurerm_storage_account.this.id
  description = "The ID of the created Storage Account."
}

output "storage_account_name" {
  value       = azurerm_storage_account.this.name
  description = "The name of the created Storage Account."
}

output "primary_blob_endpoint" {
  value       = azurerm_storage_account.this.primary_blob_endpoint
  description = "The primary Blob endpoint of the Storage Account."
}