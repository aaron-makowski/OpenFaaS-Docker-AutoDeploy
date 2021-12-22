#!/bin/bash

if [[ $(command -v pip3) ]] ; then 
	pip3 install -r ./install_scripts/requirements.txt
elif [[ $(command -v pip) ]] ; then 
	pip install -r ./install_scripts/requirements.txt
else
    echo ""
	echo "ERROR: Neither pip nor pip3 have been found"
	echo "Run apt update && apt -y upgrade && apt install python3-pip?"
    echo ""
fi
# Needs this pi upgrade stuff to be optional


