#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored
import hashlib
from time import sleep
import subprocess as s
from datetime import datetime

class hashGen:


    @staticmethod
    def get_input(prompt, error_msg="[-] Inavlid Input"): #Enter Input
        try:
            return input(prompt)
        except (ValueError, KeyboardInterrupt):
            print(colored(f"\n{error_msg}", "red", attrs=['bold']))
            return None
    @staticmethod
    def clear(): #Clear Terminal
        s.run("clear", shell=True)

    @staticmethod
    def hashed(): #Hashing Value
        hashGen.clear()
        date = colored(datetime.today().strftime('%Y-%m-%d %H:%M'), "red", attrs=['bold']) #Print Date

        print(f"""
=====================================
            HashGenerator
     >>> Developed By Furares <<<          
=====================================
{date}
{"-"*16}

1- MD5
2- SHA1
3- SHA256
4- SHA512
0- EXIT
    """)
        
        
        choice_input = hashGen.get_input("Enter Process ID => ") #Enter ID

        if choice_input is None:
            return
        
        try:
            choice = int(choice_input)
        except ValueError:
            print(colored("[-] Please Enter A Valid Number", "red", attrs=['bold']))
            return
        
        if choice == 0: #Exit 
        
            print(colored("Thanks For Using...", "green", attrs=['bold']))
            sleep(0.5)
            return
        
        if choice == 1: #MD5

            value = hashGen.get_input("Enter Value : ")
            if not value:
                return
            rhash = hashlib.md5()
            rhash.update(value.encode())
            result = (colored(rhash.hexdigest(), "green", attrs=['bold']))
            print(f"[+] Hash : {result}")
            return
        
        if choice == 2: #SHA1
            value = hashGen.get_input("Enter Value : ")
            if not value:
                return
            rhash = hashlib.sha1()
            rhash.update(value.encode())
            result = (colored(rhash.hexdigest(), "green", attrs=['bold']))
            print(f"[+] Hash : {result}")
            return
        
        if choice == 3: #SHA256

            value = hashGen.get_input("Enter Value : ")
            if not value:
                return
            
            rhash = hashlib.sha256()
            rhash.update(value.encode())
            result = (colored(rhash.hexdigest(), "green", attrs=['bold']))
            print(f"[+] Hash : {result}")
            return
        
        if choice == 4: #SHA512
            
            value = hashGen.get_input("Enter Value : ")
            if not value:
                return
            
            rhash = hashlib.sha512()
            rhash.update(value.encode())
            result = (colored(rhash.hexdigest(), "green", attrs=['bold']))
            print(f"[+] Hash : {result}")
            return
        
        else:
            print(colored("[-] Invalid Choice", "red", attrs=['bold']))
            return