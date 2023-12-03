See: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-modified-workspaces

# Call
## http
```
GET https://api.powerbi.com/v1.0/myorg/admin/workspaces/modified?modifiedSince=2023-12-02T05%3A51%3A30.0000000Z
```

## Powershell cmdlet
See [ README](../../README.md)

No cmdlet available

# Important
Use without the optional modifiedSince parameter to return a list of all workspaces without the pagination required as part of [Groups GetGroupsAsAdmin](../Groups-GetGroupsAsAdmin/detail.md) API


# Issues experienced
None