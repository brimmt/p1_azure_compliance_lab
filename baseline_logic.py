from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.network import NetworkManagementClient
import os
from dotenv import load_dotenv;
load_dotenv();


# Okay so this creates the client that can access the top level resources in the subscription
# Initialize the Azure credentials and clients
credential = DefaultAzureCredential();
# I can access top-level resources in the subscription
resource_client = ResourceManagementClient(credential, os.getenv("AZURE_SUBSCRIPTION_ID"));
# This creates the client that can access storage resources in the subscription
# Managment level client for storage resources
storage_client = StorageManagementClient(credential, os.getenv("AZURE_SUBSCRIPTION_ID"));
network_client = NetworkManagementClient(credential, os.getenv("AZURE_SUBSCRIPTION_ID"));




# Baseline Conditions

 # Resource Tag Rules

# RULE-001 - Enviroment Tag
for resource in resource_client.resources.list():
   tag = resource.tags or {}  #  <- tags are returned as dictionaires
     
   if 'environment' not in tag:
        print("Failed RULE-001 |", resource.name, "is missing the environment tag");
   else:
        print("Passed RULE-001 |", resource.name, "has the environment tag");

print("----------------------------------------------------");
print();

# RULE-002 - Owner Tag
for resource in resource_client.resources.list():
    tag = resource.tags or {};
    
    if "owner" not in tag:
        print("Failed RULE-002 |", resource.name, "is missing the 'owner' tag");
    else:
        print("Passed RULE-002 |", resource.name, "has the 'owner' tag");

print("----------------------------------------------------");
print();

# RULE-003 - Source Tag
for resource in resource_client.resources.list():
    tag = resource.tags or {};

    if "source" not in tag:
        print("Failed RULE-003 |", resource.name, "is missing the 'source' tag");
    else:
        print("Passed RULE-003 |", resource.name, "has the 'source' tag")

print("----------------------------------------------------");
print();

# RULE-004 - Deleteion Protection on Storage Accounts
for storage_account in storage_client.storage_accounts.list():
    service_properties = storage_client.blob_services.get_service_properties(
        resource_group_name=storage_account.id.split("/")[4],
        account_name=storage_account.name,
        
    )
    if service_properties.delete_retention_policy and service_properties.delete_retention_policy.enabled:
        print("Passed RULE-004 |", storage_account.name, "has delete protection enabled.");
    else:
        print("Failed RULE-004 |", storage_account.name, "is missing delete protection.");

    
print("----------------------------------------------------");
print();
# RULE-005 - Shared Key Access
# check shared key access for storage accounts
for storage_account in storage_client.storage_accounts.list():
    if storage_account.allow_shared_key_access:
        print("Failed RULE-005 |", storage_account.name, "storage account key access must be disabled.")
    else:
        print("Passed RULE-005 |", storage_account.name, "storage account key access is disabled.");

print("----------------------------------------------------");
print();


#RULE-006 - Storage account should not allow public network access
# check virtual network

for storage_account in storage_client.storage_accounts.list():
    if storage_account.properties.public_network_access == "Enabled":
        print("Failed RULE-006 |", storage_account.name, "allows public network access.");
    else:
        print("Passed RULE-006 |", storage_account.name, "does not allow public network access.");
print("----------------------------------------------------");
print();


#RULE-07 - Access Tier

for storage_account in storage_client.storage_accounts.list():
    if storage_account.access_tier == "Hot":
        print("Passed RULE-07 |", storage_account.name, "has access tier set to Hot.");
    else:
        print("Failed RULE-07 |", storage_account.name, "does not have access tier set to Hot.");

print("----------------------------------------------------");
print();















