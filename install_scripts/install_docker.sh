#!/bin/bash

if [[ "$EUID" -ne 0 ]]; then
	echo "This installer needs to be run with superuser privileges."
	exit
fi

# install docker if not installed
if ! command -v docker; then
    echo "Docker not installed, installing now..."
    echo ""
    curl -sSL https://get.docker.com/ | sh
fi
if ! command -v dockerd; then
        echo ""
        apt install docker.io
        echo ""
fi
echo "Adding your user to the docker group for non root access"
sudo usermod -aG docker $USER 
echo ""
echo "Docker install finished"
echo ""
