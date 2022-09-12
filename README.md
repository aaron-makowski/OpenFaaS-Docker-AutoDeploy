Self Hosted Serverless Bootstrapper: Docker + FaaSD + Auto Deploy - Shell Script installs and launches Python TUI

# OpenFaaS Docker AutoDeploy Script
 - Tested on WSL and Linux

# TUI Options
## Top Level Choices
- Install Docker, Login, Start on Boot
- Install FaaSD Server, faas-cli, test faasd)
- Express Install: Do all of the above
- Util: Auto-Deploy OpenFaaS function(s) from a folder
  
## Docker Choices  
- Install Docker
- Start Docker on Ubuntu using systemd
- Start Docker with init.d (eg. WSL2 Ubuntu)
- Login to Docker
- Express Setup: Do all of the above
  
## OpenFaaS Choices
- Install `faasd` server locally for testing functions  
- Test local faasd deployment using the python3 template
- Do all of the above
  
## Auto Deploy Choices
- Auto-Deploy OpenFaaS function(s) from monorepo/src/faas_functions
- Manually input path containing the function(s) to deploy...
