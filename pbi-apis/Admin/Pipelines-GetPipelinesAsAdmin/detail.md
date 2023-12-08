As pipelines are not returned in the workspace context this API will need to be run to help build up a full(ish) view of your Power BI estate. 


# Details
## REST API
See: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/pipelines-get-pipelines-as-admin

```http
GET https://api.powerbi.com/v1.0/myorg/admin/pipelines?%24expand=users%2Cstages
```


## Powershell cmdlet
See [ README](../../README.md)

No cmdlet available

# Important
Requires itterative call when you have more than 5,000 pipelines

# Issues experienced
None

# Observations
* The name of the pipeline phase is not returned in the response only the order

