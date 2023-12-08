import os 
import sys
import json
import requests

# Define inputs
outputpath = "scriptoutput/pbi-apis/Admin/Groups-GetGroupsAsAdmin/"

# Create local output directory if not exists
if not os.path.exists(outputpath):  
    os.makedirs(outputpath) 

url = 'https://api.powerbi.com/v1.0/myorg/admin/groups?$top=100&$expand=users,reports,dashboards,datasets,dataflows,workbooks'


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
 
