#!/bin/bash

# Because faas-cli push needs to take built docker images into docker hub registry
username=""
while :
do
    username=docker info | grep "Username:"
    username=${username##Username: }
    #echo "$username"
    if [ ${#username} -gt 0 ]; then
        #echo "Docker Username: $username"
        # Prompt the user for confirmation of docker Username
        read -p "Confirm Username: [y/N] $username" response

        #todo upgrade this to being able to convert string to lower
        if [ $response="Y" -o $response="y" -o $response="yes" -o $response="Yes" -o $response = "YES" -o $response = "ye" -o $response = "YE" -o $response = "Ye"]; then
            echo "Docker Login Script Finished."
            break
        else
            echo ""
            echo "Please log in to your docker account"
            docker login
            # check if success
            username=docker info | grep "Username:"
            username=${username##Username: }
            if $username; then
                break
            else
                echo ""
                echo "Username not found, Retrying..."
            fi
        fi
    #elif username is not present aka length 0
    else # this is also a duplicate of the above code
        echo "Please log in to your docker account"
        docker login
        # check if success and sore username
        username=docker info | grep "Username:"
        username=${username##Username: }
        if $username; then
            break
        else
            echo ""
            echo "Username not found, Retrying..."
        fi
    fi
done
