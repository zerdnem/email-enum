# Email-Enum
[![Version](https://img.shields.io/badge/Version-v1.2-brightgreen.svg)](https://shields.io/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://shields.io/)
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
* Proxybroker
* Pysocks

## Installation
### Linux

```
git clone https://github.com/Frint0/email-enum.git
cd email-enum
chmod +x setup.sh
./setup.sh
```

### Windows (Docker)

```
docker build -t emailenum .
docker run --rm -it emailenum <target email>
```

## Usage

`python3 check.py email@gmail.com` or `./check.py email@gmail.com`

## To-Do's

* More Websites
* Username Enumeration
* Increased Verbosity
* ~~More arguments~~
* ~~Non-Headless mode~~
* ~~Integrate automatically checking via pwndb~~
* Add support for Socks proxy

*and much more...*

## Proxy
The option `--proxy` uses [Proxybroker](https://github.com/constverum/ProxyBroker) which will run a local proxy server on port 8888 and request 5 HTTPS proxies. You don't need to search for public proxies, everything is done automatically. Note that proxies are public and often in the headers you send your real IP to the server.

## PwnDB
PwnDB is a TOR service which contains
data from 1.4 billion breach compilations. Before using `--pwndb` ensure that service tor has been 
installed, started and listening 9050 port

Results `python check.py somebody@example.com --pwndb`


![Demo Result](http://i.piccy.info/i9/5916bd8f70f9b152a41c4b6693de6e57/1556956944/257875/1315967/screen111.png)

## Disclaimer

The use of the email-enum is COMPLETE RESPONSIBILITY of the END-USER. Developers assume NO liability and are NOT responsible for any misuse or damage caused by this program.
Email-enum is done entirely via web scraping, if a website changes its element variables or layout, you might need to 
wait for an updated version of Email-Enum or feel free to contribute.
