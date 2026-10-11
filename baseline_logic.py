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
def check_environment_tag(resource):
    
        tags = resource.tags or {}  #  <- tags are returned as dictionaires
        return {
            "rule": "RULE-001",
            "resource": resource.name,
            "status": "PASS" if "environment" in tags else "FAIL",
            "Remediation": "Add environment tag to the resource" if "environment" not in tags else "No remediation needed"
        }




# RULE-002 - Owner Tag
def check_owner_tag(resource):
   
    tags = resource.tags or {};
    
    return {
         "rule": "RULE-002",
         "resource": resource.name,
         "status": "PASS" if "owner" in tags else "FAIL",
         "Remediation": "Add owner tag to the resource" if "owner" not in tags else "No remediation needed"
         
    }






# RULE-003 - Source Tag
def check_source_tag(resource):
    tags = resource.tags or {}
    return {
        "rule": "RULE-003",
        "resource": resource.name,
        "status": "PASS" if "source" in tags else "FAIL",
        "Remediation": "Add source tag to the resource" if "source" not in tags else "No remediation needed"
    }




# RULE-004 - Deleteion Protection on Storage Accounts
def check_deletion_protection_blob(storage_account):
    service_properties = storage_client.blob_services.get_service_properties(
        resource_group_name=storage_account.id.split("/")[4],
        account_name=storage_account.name,
        
    )

    return{
         "rule": "RULE-004",
         "resource": storage_account.name,
         "status": "PASS" if service_properties.delete_retention_policy and service_properties.delete_retention_policy.enabled else "FAIL",
         "Remediation": "Enable delete protection on the storage account" if not (service_properties.delete_retention_policy and service_properties.delete_retention_policy.enabled) else "No remediation needed"
    }

    
# RULE-005 - Shared Key Access
# check shared key access for storage accounts
def check_shared_key_access(storage_account):
    if storage_account.allow_shared_key_access:
        return {
            "rule": "RULE-005",
            "resource": storage_account.name,
            "status": "FAIL",
            "Remediation": "Disable shared key access on the storage account"
        }
    else:
        return {
            "rule": "RULE-005",
            "resource": storage_account.name,
            "status": "PASS",
            "Remediation": "No remediation needed"
        }


#RULE-006 - Storage account should not allow public network access
# check virtual network
def check_public_network_access(storage_account):
     #TatiNote: Ai updated this part <- come back and review Tati
     is_disabled = storage_account.public_network_access == "Disabled"
     
     return {
          "rule": "RULE-006",
          "resource": storage_account.name,
          "status": "FAIL" if not is_disabled else "PASS",
          "Remediation": "Disable public network access on the storage account" if not is_disabled else "No remediation needed"
     }



#RULE-007 - Access Tier
def check_access_tier(storage_account):

     #TatiNote: try it on my own here
     is_hot = storage_account.access_tier == "Hot"
     
     return {
          "rule": "RULE-007",
          "resource": storage_account.name,
          "status": "PASS" if is_hot else "FAIL",
          "Remediation": "Set access tier to Hot" if is_hot else "No remediation needed"
     }




# Add to results list
def update_results_list():
    results = []
    # lets add the general resources first
    for resource in resource_client.resources.list():
            results.append(check_environment_tag(resource))
            results.append(check_owner_tag(resource))
            results.append(check_source_tag(resource))

    for storage_account in storage_client.storage_accounts.list():
            results.append(check_deletion_protection_blob(storage_account))
            results.append(check_shared_key_access(storage_account))
            results.append(check_public_network_access(storage_account))
            results.append(check_access_tier(storage_account))

    return results


print(update_results_list())





