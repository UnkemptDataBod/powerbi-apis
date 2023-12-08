See: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result

This is the end call of a series that need to be executed. 

```mermaid
sequenceDiagram
    autonumber
    Caller-->>Admin - WorkspaceInfo GetModifiedWorkspaces: GET
    activate Admin - WorkspaceInfo GetModifiedWorkspaces
    Admin - WorkspaceInfo GetModifiedWorkspaces->>Caller: List of workspaces
    deactivate Admin - WorkspaceInfo GetModifiedWorkspaces
    loop every 100 workspaces
    Caller->>Admin - WorkspaceInfo PostWorkspaceInfo: POST (With workspace IDs)
    activate Admin - WorkspaceInfo PostWorkspaceInfo
    Admin - WorkspaceInfo PostWorkspaceInfo->>Caller: scanId
    deactivate Admin - WorkspaceInfo PostWorkspaceInfo
    loop Until "status": "Succeeded"
        Caller-->>Admin - WorkspaceInfo GetScanStatus: GET (Based on scanID returned from post)
        activate Admin - WorkspaceInfo GetScanStatus
       Admin - WorkspaceInfo GetScanStatus->>Caller: status
        deactivate Admin - WorkspaceInfo GetScanStatus
    end
    Caller-->>Admin - WorkspaceInfo GetScanResult: GET (Based on scanID returned from post)
    activate Admin - WorkspaceInfo GetScanResult
    Admin - WorkspaceInfo GetScanResult->>Caller: Payload
    deactivate Admin - WorkspaceInfo GetScanResult
    end
```

For the purposes of the docs it is assumed you have added the optional parameters on the "Admin - WorkspaceInfo PostWorkspaceInfo" call
* datasetExpressions=true
* datasetSchema=true
* datasourceDetails=true
* getArtifactUsers=true
* lineage=true


# Call
## REST API
```
GET https://api.powerbi.com/v1.0/myorg/admin/workspaces/scanResult/f676712d-02af-4abf-ac83-6861e0d0cad7
```
Random scan guid above

## Powershell cmdlet
See [ README](../../README.md)

No cmdlet available

# Important
* This a large response which is largely undocumented, the schema almost certianly will deviate!


# Issues experienced
* The documentation provided is very far away from the reponse of this API