if (Get-Module -ListAvailable -Name MicrosoftPowerBIMgmt) {
    
} 
else {
    Install-Module -Name MicrosoftPowerBIMgmt 
}

Login-PowerBIServiceAccount
 
Get-PowerBICapacity -Scope Organization -ShowEncryptionKey

Disconnect-PowerBIServiceAccount