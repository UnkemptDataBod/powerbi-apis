if (Get-Module -ListAvailable -Name MicrosoftPowerBIMgmt) {
    
} 
else {
    Install-Module -Name MicrosoftPowerBIMgmt 
}

Login-PowerBIServiceAccount
 
Get-PowerBIActivityEvent -StartDateTime 2023-12-16T00:00:00 -EndDateTime 2023-12-16T23:59:59

Disconnect-PowerBIServiceAccount