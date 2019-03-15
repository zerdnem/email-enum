# Email-Enum
[![Version](https://img.shields.io/badge/Version-v0.5-brightgreen.svg)](https://shields.io/)
[![Status](https://img.shields.io/badge/Status-Initial-brightgreen.svg)](https://shields.io/)
[![Platform](https://img.shields.io/badge/Platform-Linux/Windows-lightgrey.svg)](https://shields.io/)
[![Browser](https://img.shields.io/badge/Browser-Firefox-brightgreen.svg)](https://shields.io/)
[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Email-Enum searches mainstream websites and tells you if an email is registered!**

![Demo Photo](https://raw.githubusercontent.com/Frint0/email-enum/master/demo.png)

## Dependencies
* Firefox
* Selenium => 3.14
* Click => 7.0
* Termcolor => 1.1
* PyFiglet => 0.8

## Installation

Do not run **setup.sh** as root!

```
git clone https://github.com/Frint0/email-enum.git
cd email-enum
chmod +x setup.sh
./setup.sh
```

## Usage

`python3 check.py email@gmail.com` or `./check.py email@gmail.com`

## To-Do's

* More Websites
* Username Enumeration
* Increased Verbosity
* More arguments

*and much more...*

## Dockerizing 

```
docker build C:\email\enum\path\dockerfile
docker run <imagename> <target email>
```

P.S. The docker file is geared torwards Windows users who want to use Email-Enum.

## Disclaimer

This program is done entirely by web scraping, if a website changes its element variables or layout, you might need to wait for an updated version of Email-Enum or feel free to contribute.
