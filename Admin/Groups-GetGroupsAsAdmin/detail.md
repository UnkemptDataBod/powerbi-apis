# Call
```http
GET https://api.powerbi.com/v1.0/myorg/admin/groups?%24top=100&expand=users%2Creports%2Cdashboards%2Cdatasets%2Cdataflows%2Cworkbooks
```

- Requires itterative call when you have more than 5,000 workspaces

# Issues experienced
* Expand has no impact
    * Suspect this is a local issue
* GIT settings not returned
* Domain not returned
* hasWorkspaceLevelSettings has no reference