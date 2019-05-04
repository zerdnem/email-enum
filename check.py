#!/usr/bin/python3
import subprocess
import sys

import click
import pyfiglet
from termcolor import colored

from pwn_db import PwnDb
from sites import Check


def ascii_banner():
    banner = pyfiglet.figlet_format("Email Enum")
    return banner


@click.command()
@click.argument('email', nargs=1)
@click.option('--output', help='Output results into file')
@click.option('--proxy', is_flag=True, help='Use proxybroker')
@click.option('--non-headless', is_flag=True, help='Non headless mode')
@click.option('--pwndb', is_flag=True, help='Check leaks in PwnDB')
def email_enum(email, output, proxy, non_headless, pwndb):
    print(colored(ascii_banner(), 'magenta'))
    print(colored("Author: ", 'green') + "Frinto, yevgen2020")
    print(colored("Version: ", 'green') + colored("v1.2", 'yellow'))
    print("\n\n")
    try:
        subprocess.check_output(['which', 'firefox'])
    except subprocess.CalledProcessError as exc:
        print(colored("Firefox is not installed or isn't in PATH, exiting...", 'yellow'))
        sys.exit()

    if proxy:
        proxy_broker = subprocess.Popen(['python', 'proxy.py'])
    else:
        proxy_broker = None

    checker = Check(email, proxy, non_headless)

    excl = colored("[!] ", "yellow")
    excl2 = colored("[*] ", "magenta")
    excl3 = colored("[pwndb] ", "magenta")

    print(excl + "Checking Instagram...")
    insta_response = checker.instagram_check()

    print(excl + "Checking Twitter...")
    twit_response = checker.twitter_check()

    print(excl + "Checking Snapchat...")
    snap_response = checker.snapchat_check()

    print(excl + "Checking Facebook...")
    face_response = checker.facebook_check()

    print(excl + "Checking Google/Youtube...")
    gooyou_response = checker.yougoogle_check()

    print(excl + "Checking Twitch...")
    twitch_response = checker.twitch_check()

    if pwndb:
        print(excl + "Checking PwnDB...")
        db_check = PwnDb(email)
        db_response = db_check.check()

    if proxy_broker:
        proxy_broker.kill()
    checker.quit_selenium()

    print("\n\n")
    results = pyfiglet.figlet_format("Results")
    print(colored(results, "green"))
    print(excl2 + "Instagram: " + insta_response)
    print(excl2 + "Twitter: " + twit_response)
    print(excl2 + "Snapchat: " + snap_response)
    print(excl2 + "Facebook: " + face_response)
    print(excl2 + "Google/Youtube: " + gooyou_response)
    print(excl2 + "Twitch: " + twitch_response)

    if db_response:
        if type(db_response) is str:
            print(excl3 + db_response)
        if type(db_response) is list:
            for i in db_response:
                print(excl3 + i)
    if output:
        outputfile = open(output, "a")
        listout = ["Instagram: " + insta_response, "Twitter: " + twit_response, "Snapchat: " + snap_response,
                   "Facebook: " + face_response, "Google/Youtube: " + gooyou_response, "Twitch: " + twitch_response]
        outputfile.writelines((i + '\n' for i in listout))
        outputfile.close()
        sys.exit()
    else:
        sys.exit()


if __name__ == '__main__':
    email_enum()
