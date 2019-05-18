#!/usr/bin/env bash
if [[ $EUID -eq 0 ]]; then
	echo "This script must NOT be run as root" 1>&2
		exit 1
	fi

pip3 install click --user
pip3 install termcolor --user
pip3 install selenium --user
pip3 install pyfiglet --user
pip3 install proxybroker --user
pip3 install pysocks --user
pip3 install Flask --user
pip3 install Flask-Caching --user
mkdir -p ~/.local/bin/

# Install geckodriver on linux machines (64-bit or 32-bit)
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	if [ `getconf LONG_BIT` = "64" ]
	then
		printf "Downloading geckodriver for linux64\n"
		wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz -q --show-progress
		tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
		chmod +x geckodriver

	else
		printf "Downloading geckodriver for linux32\n"
		wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz -q --show-progress
		tar -xvzf geckodriver-v0.24.0-linux32.tar.gaz
		chmod +x geckodriver
	fi
	mv geckodriver ~/.local/bin/
	printf "\n[*] Setup completed\n\n"
	printf "Usage: python3 check.py email@gmail.com or ./check.py email@gmail.com\n\n"
	exit 1
fi

mv geckodriver ~/.local/bin/geckodriver
