This API is not one that should be used to catalog your content as the REST API [WorkspaceInfo-GetScanResult](../WorkspaceInfo-GetScanResult/detail.md) superscedes this API in terms of completeness of data.


# Details
## REST API
See: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/groups-get-groups-as-admin

```http
GET https://api.powerbi.com/v1.0/myorg/admin/groups?%24top=100&expand=users%2Creports%2Cdashboards%2Cdatasets%2Cdataflows%2Cworkbooks
```


## Powershell cmdlet
See https://learn.microsoft.com/en-us/powershell/module/microsoftpowerbimgmt.workspaces/get-powerbiworkspace?view=powerbi-ps

Generally the parameters are faithful to the API endpoint
```powershell
Get-PowerBIWorkspace -Scope Organization -expand Reports,Datasets,dashboards,dataflows,workbooks -First 100
```

There is a catchall for content that *seems* somewhat more resilient to change
```powershell
Get-PowerBIWorkspace -Scope Organization -expand All -First 100
```

# Important
Requires itterative call when you have more than 5,000 workspaces

# Issues experienced
* hasWorkspaceLevelSettings has no reference (via REST API, Powershell command has no representation of this)

# Observations
* REST API - where present, users, upstreamDatasets and subscriptions as part of content return no data
* cmdlet - Users are auto expanded 
* GIT settings not returned
* Domain not returned

