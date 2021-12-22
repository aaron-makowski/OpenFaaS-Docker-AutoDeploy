#!/bin/bash

BASE_DIR=./install_scripts

docker_username=$("$BASE_DIR"/get_logged_in_docker_username.sh)

# User input path
while :
do
    read -p "Input path of folder you want to auto deploy the OpenFaaS functions in" FUNCS_DIR
    if [ ! -d "$FUNCS_DIR" ]; then
       echo ""
       echo "Path not found: $FUNCS_DIR"
       echo ""
    else
       break
    fi
done


# Make this user changable
all_function_folders=`ls $FUNCS_DIR`
# search all folders in faas functions folder
for folder in $all_function_folders
do
    if [ -d "$folder" -a ! "$folder"="template" -a ! "$folder"="build" ]; then # if its a folder
        function_yml_filename="$folder.yml"
        # echo "function yml file $function_yml_filename"
        if test -f $function_yml_filename; then # if .yml file for function exists in the folder
            if ! faas-cli list | grep "$folder"; then # if function not in deployed list
                # Replace image: function_name:latest with the same but prefixed with our dokcer username
                python3 "$SCRIPTS_DIR"/insert_docker_username_into_yml_file.py "$docker_username" "$FUNCS_DIR"/"$function_yml_filename"

                # Build docker image, send it to docker hub, deploy image to local faasd
                faas-cli build  -f "$function_yml_filename"
                faas-cli push   -f "$function_yml_filename"
                faas-cli deploy -f "$function_yml_filename"
                # rip function name from yml filepath
                function_name="${folder##/*/}"
                # echo "function name $function_name"
                if faas-cli list | grep -q "$function_name"; then
                    echo "Auto-Deploy to FaaSD Successful for: $function_name" | faas-cli invoke "$function_name"
                    echo "$function_name logs:"
                    faas-cli logs --follow=false "$function_name"
                else
                    echo "Auto-Deploy to FaaSD Failed for: $function_name"
                    echo "and should be missing from the following list of deployed functions"
                    echo ""
                    echo ""
                    faas-cli list
                fi
            else
                echo "Function: $folder is already deployed."
                echo "and should be in the following list of deployed functions"
                echo ""
                echo ""
                faas-cli list
            fi
        else
            echo "$function_yml_filename file not found in the function folder: $folder"
        fi
    fi
done
