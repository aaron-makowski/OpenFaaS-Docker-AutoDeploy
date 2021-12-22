#!/bin/bash

# Set dir as variable
BASE_DIR=./install_scripts

username=$("$BASE_DIR"/get_logged_in_docker_username.sh)
echo "$username"

if [ "$username" = "DockerNotLoggedIn" ]; then
   echo "You need to log in to docker before deploying a function"
   echo "Use `docker login` or `python3 run_installer.py` and use the Login to Docker option"
   exit 0
fi

mkdir -p  "$BASE_DIR"/faas_test_funcs
FUNCS_DIR="$BASE_DIR"/faas_test_funcs
cd "$FUNCS_DIR"

# Create a hello world python function from the python3 template. [a-z] name
faas-cli new testpythonfaas --lang python3

# Replace image: function_name:latest with the same but prefixed with our dokcer username
python3 ../insert_docker_username_into_yml_file.py "$username" ./testpythonfaas.yml

# Build docker image, send it to docker hub, deploy image to local faasd
faas-cli build  -f ./testpythonfaas.yml
faas-cli push   -f ./testpythonfaas.yml
faas-cli deploy -f ./testpythonfaas.yml

# Invoke and actually test the python3 function
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Python3 Template Auto-Deploy to FaaSD Successful" | faas-cli invoke testpythonfaas
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
faas-cli logs --follow=false testpythonfaas #Follow is false to avoid getting stuck in the running log
