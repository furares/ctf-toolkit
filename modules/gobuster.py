#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as s
from time import sleep
from termcolor import colored
import os


class gobusterScan:
    
    
    @staticmethod
    def get_input(prompt,error_msg="[-] Invalid Input"):
        try:
            return input(prompt)
        except (ValueError, KeyboardInterrupt):
            print(colored(f"\n{error_msg}", "red", attrs=['bold']))
            return None
        
    
    @staticmethod
    def main_menu():

        print("""
=====================================================================
1- Gobuster dir -u https://your_url -w wordlist_path
2- Gobuster dir -u https://your_url -w wordlist_path -x php,html,htm
3- Gobuster dir -u https://your_url -w wordlist_path -q 
4- Gobuster dns -d https://your_url -w wordlist_path
0- Exit
=====================================================================
                  """)

        choice_input = gobusterScan.get_input("Enter Process ID => ")
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
            return
            
        if choice == 1:
            url = gobusterScan.get_input("Enter Url (ex. https://host_name) : ")
            if not url:
                return
            
            wordlist  = gobusterScan.get_input("Enter Wordlist Path : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("[-] Wordlist Not Found", "red", attrs=['bold']))
                return
            s.run("clear", shell=True)                        
            s.run(["sudo", "gobuster", "dir", "-u", url, "-w", wordlist])

        if choice == 2:

            url = gobusterScan.get_input("Enter Url (ex. https://hostname) : ")
            if not url:
                return

            wordlist = gobusterScan.get_input("Enter Wordlist Path : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("[-] Wordlist File Not Found", "red", attrs=['bold']))
                return

            s.run("clear", shell=True)
            s.run(["sudo", "gobuster", "dir", "-u", url, "-w", wordlist, "-x", "php,html,htm"])

        if choice == 3:

            url = gobusterScan.get_input("Enter Url (ex. https://host_name) : ")
            if not url:
                return
            
            wordlist = gobusterScan.get_input("Enter Wordlist Path : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("[-] Wordlist File Not Found", "red", attrs=['bold']))
                return
            
            s.run("clear", shell=True)
            s.run(["sudo", "gobuster", "dir", "-u", url, "-w", wordlist, "-q"])

        if choice == 4:

            url = gobusterScan.get_input("Enter Url (ex. https://host_name) : ")
            if not url:
                return
            
            wordlist = gobusterScan.get_input("Enter Wordlist Path : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("Wordlist File Not Found", "red", attrs=['bold']))
                return
            
            s.run("clear", shell=True)
            s.run(["sudo", "gobuster", "dns", "-d", url, "-w", wordlist])

        else:
            print(colored("[-] Invalid choice. Please try again.", "red", attrs=['bold']))

        
        
