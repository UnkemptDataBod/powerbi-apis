As capacities are not returned in the workspace context this API will need to be run to help build up a full(ish) view of your Power BI estate. 


# Details
## REST API
https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-capacities-as-admin

```http
GET https://api.powerbi.com/v1.0/myorg/admin/capacities?expand=tenantKey
```

## Powershell cmdlet
See https://learn.microsoft.com/en-us/powershell/module/microsoftpowerbimgmt.capacities/get-powerbicapacity?view=powerbi-ps

Generally the parameters are faithful to the API endpoint
```powershell
Get-PowerBICapacity -Scope Organization -ShowEncryptionKey
```

# Important
None

# Issues experienced
None

# Observations
None


