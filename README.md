
# powerbi-apis
This is initially to provide a base for schema validation and as a reference for future usage of the APIs. 

The Power BI APIs are not all that are required as the Power BI ecosystem extends beyond the REST APIs as documented [here](https://learn.microsoft.com/en-us/rest/api/power-bi/)

# General
## Rest API
Have added a python script to call the apis, you will need to generate a bearer token though for the power bi service. 
See https://learn.microsoft.com/en-us/rest/api/power-bi/

If you want to *cheat* you can grab a bearer token from the 'try it' pane of the REST API docs
See https://learn.microsoft.com/en-us/rest/api/power-bi/admin/groups-get-groups-as-admin#code-try-0

## Powershell cmdlet
Have included the commands for powershell as it is implied [here](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-reference) that there is a parity between the cmdlets and the APIs however there are differences as highlighted in the Groups-GetGroupsAsAdmin [detail.md](/pbi-rest-apis/Groups-GetGroupsAsAdmin/detail.md) file.

To execute the powershell scripts you need to install [MicrosoftPowerBIMgmt](https://www.powershellgallery.com/packages/MicrosoftPowerBIMgmt/1.2.1111) and login

```powershell
Install-Module -Name MicrosoftPowerBIMgmt 

Login-PowerBIServiceAccount
```
Generally there is loose parity of feature when the feature has both an administrative and user based context to the API however powershell commands have been included for reference

## .net Client Library
Would welcome contributions

# General resources used
https://guidgenerator.com/

https://www.jsongenerator.io/schema

# Other useful references
* [microsoft / powerbi-powershell](https://github.com/microsoft/powerbi-powershell) repo

* [microsoft /  PowerBI-CSharp](https://github.com/microsoft/PowerBI-CSharp) repo