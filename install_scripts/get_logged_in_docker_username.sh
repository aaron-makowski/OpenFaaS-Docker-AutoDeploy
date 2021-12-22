#!/bin/bash

USERNAME=$(docker info | grep "Username:")

if [ ${#USERNAME} -gt 5 ]; then
    echo ${USERNAME##" Username: "}
else
    echo "DockerNotLoggedIn"
fi
