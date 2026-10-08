terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
}


resource "azurerm_resource_group" "rg" {
  name     = "test-rg"
  location = "East US"
  tags = {
    environment = "test"
    source      = "terraform"
  }
}

resource "azurerm_storage_account" "storage" {
  name                     = "rgteststorageaccount"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = "centralus"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "dev"
    source      = "terraform"
  }
}

resource "azurerm_storage_container" "container" {
  name                  = "test-container"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}


resource "azurerm_storage_blob" "blob" {
  name                   = "test-blob"
  storage_account_name   = azurerm_storage_account.storage.name
  storage_container_name = azurerm_storage_container.container.name
  type                   = "Block"
  source                 = "files/test.txt"
}


resource "azurerm_storage_blob" "another_blob" {
  name                   = "another-blob"
  storage_account_name   = azurerm_storage_account.storage.name
  storage_container_name = azurerm_storage_container.container.name
  type                   = "Block"
  source                 = "files/another_text.txt"
}


resource "azurerm_virtual_network" "vnet" {
  name                = "test-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "westus"
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "test-subnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}