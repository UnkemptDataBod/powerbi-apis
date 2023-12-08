if (Get-Module -ListAvailable -Name MicrosoftPowerBIMgmt) {
    
} 
else {
    Install-Module -Name MicrosoftPowerBIMgmt 
}

Login-PowerBIServiceAccount
 
Get-PowerBIWorkspace -Scope Organization -expand All -First 100

Disconnect-PowerBIServiceAccount