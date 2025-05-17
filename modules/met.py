#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as s
from time import sleep
from termcolor import colored

class metasploit:
    @staticmethod
    def start():
        print(colored("Metasploit Framework Starting...", "green", attrs=['bold']))
        sleep(0.5)
        s.run("clear", shell=True)
        s.run("sudo msfconsole", shell=True)
