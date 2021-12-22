#!/bin/bash

if [[ "$EUID" -ne 0 ]]; then
	echo "This installer needs to be run with superuser privileges."
	exit
fi

if [ $1="systemd" ]; then
	# Start docker and start it on boot
	systemctl unmask docker.socket
	systemctl unmask docker.service
	systemctl start docker.service
	echo ""
	systemctl status docker | grep "Active: active (running)"
	echo ""
	echo "Docker status should be 'Active: active (running)'"
fi
# This option in WSL2 doesnt keep docker running for more than 10 seconds
#elif [ $1="init.d" ]; then
#	service docker start
#	echo ""
#	echo "Docker status: "
#	result=`service docker status`
#	if $result="Docker is not running"; then
#		service docker restart
#		echo ""
#		echo "Docker status: "
#		result=`service docker status`
#	fi
#		echo "Docker status should be 'running'"
#		echo ""
#	if $result | grep "Docker is not running"; then
#		echo "Error starting docker with init.d"
#		echo ""
#	fi
#fi
