#!/usr/bin/python3
import os
import sys
import click
from termcolor import colored
import subprocess
import pyfiglet

def asciiBanner():
    banner = pyfiglet.figlet_format("Email Enum")
    return banner

@click.command()
@click.argument('email', nargs=1)
@click.option('--output', help='Output results into file')
def emailEnum(email, output):
    print(colored(asciiBanner(), 'magenta'))
    print(colored("Author: ", 'green') + "Frinto")
    print(colored("Version: ", 'green') + colored("v1.0", 'yellow'))
    print("\n\n")
    try:
        firefox_check = subprocess.check_output(['which', 'firefox'])
    except subprocess.CalledProcessError as exc:
        print(colored("Firefox not installed or isn't in PATH, exiting...", 'yellow'))
        sys.exit()
    import sites
    excl = colored("[!] ", "yellow")
    excl2 = colored("[*] ", "magenta")
    print(excl + "Checking Instagram...")
    insta_response = sites.instagramCheck(email)
    print(excl + "Checking Twitter...")
    twit_response = sites.twitterCheck(email)
    print(excl + "Checking Snapchat...")
    snap_response = sites.snapchatCheck(email)
    print(excl + "Checking Facebook...")
    face_response = sites.facebookCheck(email)
    print(excl + "Checking Google/Youtube...")
    gooyou_response = sites.yougoogleCheck(email)
    print(excl + "Checking Twitch...")
    twitch_response = sites.twitchCheck(email) 
    sites.quitSelenium()
    print("\n\n")
    results = pyfiglet.figlet_format("Results") 
    print(colored(results, "green"))
    print(excl2 + "Instagram: " + insta_response)
    print(excl2 + "Twitter: " + twit_response)
    print(excl2 + "Snapchat: " + snap_response)
    print(excl2 + "Facebook: " + face_response)
    print(excl2 + "Google/Youtube: " + gooyou_response)
    print(excl2 + "Twitch: " + twitch_response)
    if output is not None:
        outputfile = open(output, "a")
        listout = ["Instagram: " + insta_response, "Twitter: " + twit_response, "Snapchat: " + snap_response, "Facebook: " + face_response, "Google/Youtube: " + gooyou_response, "Twitch: " + twitch_response]
        outputfile.writelines((i + '\n' for i in listout))
        outputfile.close()
        sys.exit()
    else:
        sys.exit()

emailEnum()
