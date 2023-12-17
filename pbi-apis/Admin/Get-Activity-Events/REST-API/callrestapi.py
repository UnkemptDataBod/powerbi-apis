import os 
import sys
import json
import requests

# Define inputs
outputpath = "scriptoutput/pbi-apis/Admin/Get-Activity-Events/"

# Create local output directory if not exists
if not os.path.exists(outputpath):  
    os.makedirs(outputpath) 

url = "https://api.powerbi.com/v1.0/myorg/admin/activityevents?startDateTime='2023-12-16T00:00:00.000Z'&endDateTime='2023-12-16T23:59:59.000Z'"


bearer = input("Enter bearer:")

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
 
