#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as s
from termcolor import colored
from time import sleep
from os import path

class crack_rsa:

    @staticmethod
    def get_input(prompt,err_msg="[!] Invalid Input"):
        try:
            return input(prompt)
        except (ValueError, KeyboardInterrupt):
            print(colored(f"\n{err_msg}", "red", attrs=['bold']))
            return None
    
    @staticmethod
    def crack():

        rsa_file = crack_rsa.get_input("Enter RSA File Path : ")
        if rsa_file is None:
            return
        if not path.exists(rsa_file):
            print(colored("[-] RSA File Not Found ", "red", attrs=['bold']))
            return
        
        output_file = crack_rsa.get_input("Enter Output File : ")
        if output_file is None:
            return
        
        try:
            with open(output_file, "w") as f:
                if not path.exists("ssh2john.py"):
                    print(colored("[-] ssh2john Not Found", "red", attrs=['bold']))
                s.run(["python3", "ssh2john.py", rsa_file], stdout=f)
                print(colored("[+] File Cracked...", "green", attrs=['bold']))
        except Exception as e:
            print(colored(f"Error Occurred : {e}", "red", attrs=['bold']))
            return
