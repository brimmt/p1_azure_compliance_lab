# Azure Compliance Lab Baseline

## MUST Requirements

## Resources
-----
### RULE-001 — Environment Tag
All resources that support tags must contain an `environment` tag.

Failure: FAIL

### RULE-002 — Owner Tag
All resources that support tags must contain an `owner` tag.

Failure: FAIL

### RULE-003 — Source Tag

All resources that supports tags must contain an `source` tag.

Failure: FAIL

---
## Storages
---
### RULE-004 — Delete Protection

All blob storage accounts must have "Blob soft delete" enabled. 

Failure: FAIL


### RULE-005 — Storage Key Acess
Storage account key access must be disabled. 

Failure: FAIL


### RULE-006 — Blob Network Access

Public network access must be disabled. 

Failure: FAIL




## SHOULD Requirements

### RULE-07 — Access Tier

Blob storage should have "Hot" access tier.

Failure: FAIL

