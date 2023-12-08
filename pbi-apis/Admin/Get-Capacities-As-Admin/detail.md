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
If you have more than 5000 apps you will not be able to return them all according to the API spec.

# Issues experienced
* No audience context returned
* A seperate call to [Apps-GetAppUsersAsAdmin](../Apps-GetAppUsersAsAdmin/detail.md) is required to get the app permissions
* ONLY the first 5000 apps can be returned

# Observations
* REST API - users array returned in results contains no data, potentially the intention is that you utilise [Apps-GetAppUsersAsAdmin](../Apps-GetAppUsersAsAdmin/detail.md) but this is not made clear


