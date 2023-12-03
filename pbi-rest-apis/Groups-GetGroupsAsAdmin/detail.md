See: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/groups-get-groups-as-admin

# Call
## http
```http
GET https://api.powerbi.com/v1.0/myorg/admin/groups?%24top=100&expand=users%2Creports%2Cdashboards%2Cdatasets%2Cdataflows%2Cworkbooks
```

## Powershell cmdlet
See [ README](../../README.md)
Generally the parameters are faithful to the API endpoint
```powershell
Get-PowerBIWorkspace -Scope Organization -expand Reports,Datasets,Users,dashboards,dataflows,workbooks
```
Users are auto expanded and adding "Users" to the expand param will throw an error. 

There is a catchall for content that *seems* somewhat more resilient to change
```powershell
Get-PowerBIWorkspace -Scope Organization -expand All
```

# Important
Requires itterative call when you have more than 5,000 workspaces

# Issues experienced
* Expand has no impact (http call)
    * Suspect this is a local issue
* GIT settings not returned
* Domain not returned
* hasWorkspaceLevelSettings has no reference (via http, powershell cmd has no representation of this)