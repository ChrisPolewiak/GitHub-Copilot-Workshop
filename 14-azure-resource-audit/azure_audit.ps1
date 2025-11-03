<#
.SYNOPSIS
Azure Resource Audit Script
.DESCRIPTION
This script lists selected Azure resources and exports the data to CSV and JSON files.
#>


# Ensure Az module is installed
if (-not (Get-Module -ListAvailable -Name Az)) {
    Write-Host "Installing Az module..." -ForegroundColor Yellow
    Install-Module Az -Scope CurrentUser -Force
}


Import-Module Az
Connect-AzAccount -UseDeviceAuthentication


Write-Host "Collecting Azure resource data..." -ForegroundColor Cyan


# Get Resource Groups
$resourceGroups = Get-AzResourceGroup | Select-Object ResourceGroupName, Location, Tags


# Get Virtual Machines
$vms = Get-AzVM | Select-Object Name, ResourceGroupName, Location, VmSize


# Get Storage Accounts
$storage = Get-AzStorageAccount | Select-Object StorageAccountName, ResourceGroupName, Location, Sku


# Get Web Apps
$webapps = Get-AzWebApp | Select-Object Name, ResourceGroup, Location, State


# Combine results into a custom object
$auditResults = [PSCustomObject]@{
    ResourceGroups  = $resourceGroups
    VirtualMachines = $vms
    StorageAccounts = $storage
    WebApps         = $webapps
}


# Export to files
$outputFolder = "./audit-outputs"
if (-not (Test-Path $outputFolder)) { New-Item -ItemType Directory -Path $outputFolder | Out-Null }


$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$auditResults | ConvertTo-Json -Depth 4 | Out-File "$outputFolder/azure_audit_$timestamp.json"
$resourceGroups | Export-Csv "$outputFolder/resourceGroups_$timestamp.csv" -NoTypeInformation
$vms | Export-Csv "$outputFolder/vms_$timestamp.csv" -NoTypeInformation
$storage | Export-Csv "$outputFolder/storageAccounts_$timestamp.csv" -NoTypeInformation
$webapps | Export-Csv "$outputFolder/webApps_$timestamp.csv" -NoTypeInformation


Write-Host "Audit completed! Results saved in $outputFolder" -ForegroundColor Green