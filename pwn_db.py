#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class PwnDb:
    def __init__(self, email):
        self.email = email
        self.session = requests.session()
        self.session.proxies = {
                'http': 'socks5h://localhost:9050',
                'https': 'socks5h://localhost:9050'
        }
        self.url = "http://pwndb2am4tzkvold.onion/"

    def check(self):
        if not '@' and not '.' in self.email:
            return 'Wrong email format'

        else:
            username = self.email.split("@")[0]
            domain = self.email.split("@")[1]
            request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}
            try:
                r = self.session.post(self.url, data=request_data)
                return self.parse(r.text)
            except:
                return "Can't connect to PwnDB service!"

    def parse(self, data):
        if "Array" not in data:
            return "No leaks found"
        else:
            leaks = data.split("Array")[1:]
            result = []
            for leak in leaks:
                leak_mail = leak.split("[luser] =>")[1].split("[")[0].strip() + "@" + \
                            leak.split("[domain] =>")[1].split("[")[0].strip()
                result.append('\033[32m' + 'Found ' + '\033[0m' + leak_mail + ":" +
                              leak.split("[password] =>")[1].split(")")[0].strip())

            return result
