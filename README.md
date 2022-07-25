# OpenFaaS Docker AutoDeploy Script
 Tested on WSL and Linux

 Self Hosted Serverless Bootstrapper: Docker + FaaSD + Auto Deploy - Shell Script installs and launches Python TUI
# Option Text as Arrays
top_level_choices = [  
    ' Install Docker, Login, Start on Boot',  
    ' Install FaaSD Server, faas-cli, test faasd) ',  
    ' Express Install: Do all of the above',  
    #' Util: Auto-Deploy OpenFaaS function(s) from a folder'  
    ]  
  
docker_choices = [  
    ' Install Docker',  
    ' Start Docker on Ubuntu using systemd',  
    #' Start Docker with init.d (eg. WSL2 Ubuntu)',  
    ' Login to Docker',   
    ' Express Setup: Do all of the above ']  
  
openfaas_choices = [  
    ' Install `faasd` server locally for testing functions',  
    ' Test local faasd deployment using the python3 template ',  
    ' Do all of the above']  
  
auto_deploy_choices = [  
    ' Auto-Deploy OpenFaaS function(s) from monorepo/src/faas_functions ',  
    ' Manually input path containing the function(s) to deploy...']  
