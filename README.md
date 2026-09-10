
************************************************************************
COmpute + VM Deployment + Docker installation + Azure Cli Installion
************************************************************************
az acr list --output table
az acr build -- registry cloudxeusdev --image customerportal:v2 --file Dockerfile .
Install a vm
install docker
install azure cli tool
az acr login -n cloudxeusdev
docker run -d -p 8000:8000 --name customerportal cloudxeusdev.azurecr.io/customerportal:v2
- Enable Inbound FW Rule
- Copy IP of VM and check if app is working

************************************************************************
Container Instance
- Create container inststance
		- point the acr registry (admin enabled)
		- adjust the tcp port to 8000 
- Ensure Instance is running

************************************************************************
Configure WebAPP (PAAS Service)
************************************************************************
- Disable admin permisions on the acr registry
- Create a webapp with Identity role (not the admin as its already disabled)
- Deploy and create webapp
- Copy Domain on the overview page and check if the app is running.
- Note: the local port 8000 would be mapped to port 80 automatically and its user agnostic.
************************************************************************
 triggered deployments - New Code Changes are deployed automatically
************************************************************************
Prerequesites:
      - git installation on local laptop            
			- github account creation.
      - Integrate VisualStudion to github to repository
      - Commit initial code files to github
      - Create a personal token on gitHub for various activities
      - copy and store token as it may be needed in future
      - Create a Task to build after every commit and upload new image to the container repository(below).

 

$GIT_PAT = Read-Host "Enter your GitHub PAT"

az acr task create `
  --registry vishwakosha `
  --name customerportal-build `
  --context "https://github.com/ssatisha/codex-app.git#main" `
  --file Dockerfile `
  --image "customerportal:{{.Run.ID}}" `
  --git-access-token $GIT_PAT
    
Commands:

1.set new build version config:
az webapp config container set `
    --name cloudx-customerportal `
    --resource-group rg-ai-200-dev `
    --container-image-name cloudxeusdev.azurecr.io/customerportal:cu2
2. Restart the webapp for new config to take in to effect.
az webapp restart `
    --name cloudx-customerportal `
    --resource-group rg-ai-200-dev 
	
************************************************************************
1.Check current Revision Mode of a containerApp if its Single.
az containerapp show `
   --name cloudxeus-apps `
   --resource-group rg-ai-200-dev `
   --query properties.configuration.activeRevisionsMode `
   --output tsv
2. Change the revision mode to Multiple Revision Mode (Multiple)
   az containerapp revision set-mode `
   --name cloudxeus-apps `
   --resource-group rg-ai-200-dev `
   --mode multiple `
   --output tsv
3. Update Container app with the change above
	az containerapp update `
	  --name cloudxeus-apps `
	  --resource-group rg-ai-200-dev `
	  --image cloudxeusdev.azurecr.io/customerportal@sha256:f79f6e9d3bb0bbc3a2dc775f4563f5c70d90350d502125e283b937462df1fc67 `
	  --revision-suffix v1
	  
*******************************************************
Update ACR to an existing cluster
	  
az aks update `
  --name aks-terraform `
  --resource-group aks-terraform-rg `
  --attach-acr cloudxeusdev
  
*******************************************************
