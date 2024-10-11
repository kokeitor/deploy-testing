## Vercel
create vercel.json
```sh
vercel login
vercel .
```
follow instructions on the console

## Azure github actions
create .github/workflows/deploy-azure.yml

## AZURE CLI login and create app service:
```sh
az login --user <username> --password <password>
```
or
```sh	
az login

az appservice plan create --resource-group MY_RESOURCE_GROUP --name MY_APP_SERVICE_PLAN --is-linux 
```
save console info and plan name: 
resource group : BOE-ChatBot
plan name : test-fastapi

```sh	
az webapp create --name MY_WEBAPP_NAME --plan MY_APP_SERVICE_PLAN --resource-group MY_RESOURCE_GROUP --runtime "python|3.11"
```
app name : test-fastapi-app-kokeitor

deployment center on azure abd follow steps
configure yaml github actions created by azure on your repo
checkout secrets etc
push to deploy


docs : https://docs.github.com/en/actions/use-cases-and-examples/deploying/deploying-python-to-azure-app-service

# Render 
For next testing (spiler -> too easy)