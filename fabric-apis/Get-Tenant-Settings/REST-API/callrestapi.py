import os 
import sys
import json
import requests

# Define inputs
outputpath = "scriptoutput/fabric-apis/tenantsettings/"

# Create local output directory if not exists
if not os.path.exists(outputpath):  
    os.makedirs(outputpath) 

url = 'https://api.fabric.microsoft.com/v1/admin/tenantsettings'


bearer = username = input("Enter bearer:")

headers = {
    'Authorization': 'Bearer ' + bearer,
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("Status Code: " + str(response.status_code)) 

result = response.json()
sys.stdout = open(outputpath + 'output.json','wt')
print (str(json.dumps(result, indent=4)).replace("'", "\""))
 
