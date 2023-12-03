# powerbi-apis
This is initially to provide a base for schema validation and as a reference for future usage of the APIs. 

The Power BI APIs are not all that are required as the Power BI ecosystem extends beyond the REST APIs as documented [here](https://learn.microsoft.com/en-us/rest/api/power-bi/), Powreshell cmdlets [here](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-reference)

# General
To execute the powershell scripts you need to install [MicrosoftPowerBIMgmt](https://www.powershellgallery.com/packages/MicrosoftPowerBIMgmt/1.2.1111) and login

```powershell
Install-Module -Name MicrosoftPowerBIMgmt 

Login-PowerBIServiceAccount
```
Generally there is parity of feature when the feature has both an administrative and user based context to the API

# General resources used
https://guidgenerator.com/

https://www.jsongenerator.io/schema