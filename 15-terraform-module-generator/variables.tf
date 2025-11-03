variable "storage_account_name" {
  type        = string
  description = "The name of the Storage Account to create."
}

variable "resource_group_name" {
  type        = string
  description = "The name of the existing Resource Group."
}

variable "location" {
  type        = string
  description = "Azure region where the Storage Account will be deployed."
  default     = "westeurope"
}

variable "account_tier" {
  type        = string
  description = "The performance tier of the storage account (Standard/Premium)."
  default     = "Standard"
}

variable "replication_type" {
  type        = string
  description = "The replication type (LRS/GRS/RAGRS/ZRS)."
  default     = "LRS"
}