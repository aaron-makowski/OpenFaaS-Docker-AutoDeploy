#!/bin/bash

if [[ "$EUID" -ne 0 ]]; then
	echo "This installer needs to be run with superuser privileges."
	exit
fi

apt update -y

# Remove current faasd installation if it exists with the current version
version=""
echo "Finding latest version from GitHub"
version=$(curl -sI https://github.com/openfaas/faasd/releases/latest | grep -i "location:" | awk -F"/" '{ printf "%s", $NF }' | tr -d '\r')
if [ ! $version ]; then
  echo "Failed while attempting to get latest version for removing old installs"
  exit 1
fi
rm -rf /tmp/faasd-${version}-installation
rm -rf /home/$USER/.faasd

echo "LOOK HERE FUCEKRKERHJNWEJKBRJKABTRKHJAEBKHTGBAEKJFVBAEKWJBF"
rm -rf /var/lib/faasd/
ls -a /var/lib/faasd


# Clone FaaSD
mkdir /home/$USER/.faasd
git clone https://github.com/openfaas/faasd /home/$USER/.faasd

# Install faasd via included shell script
chmod +x /home/$USER/.faasd/hack/install.sh
/bin/bash /home/$USER/.faasd/hack/install.sh

# Finished
echo ""
echo "Finished installing FaaSD to /home/$USER/.faasd"
echo ""
