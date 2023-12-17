This API gives information about actions that occur within the power bi service
> [!NOTE]  
> Events triggered from Power BI Desktop or Paginated report builder are not captured!

> [!WARNING]  
> The sample file is limited in scope and does not include all possible combinations of output

# Details
## REST API
See: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-activity-events

```http
GET https://api.powerbi.com/v1.0/myorg/admin/activityevents?startDateTime='2019-08-13T07:55:00.000Z'&endDateTime='2019-08-13T08:55:00.000Z'
```


## Powershell cmdlet
See https://learn.microsoft.com/en-us/powershell/module/microsoftpowerbimgmt.admin/get-powerbiactivityevent?view=powerbi-ps

The parameters are more limited than the rest API by virtue of the $filter URI parameter

```powershell
Get-PowerBIActivityEvent -StartDateTime 2019-08-10T14:35:20 -EndDateTime 2019-08-10T18:25:50
```


# Important
* *ONLY* 30 days histroy can be returned using the APIs
* The date part of both parameters *MUST* be the same date
* The REST API requires you to utilise the continuation token to collect all data for the specified timeframe

# Issues experienced
* There is a delay in the availability of data via the API and I experienced events arriving at differing delays while testing

# Observations
* Unlike the other Powershell commandlets there is a need to explicitly add the "-ResultType JsonObject" optional parameter, this has not been done in the examples or scripts as the raw json output is more usable.
* Attributes drop in an out of the payload over time.

