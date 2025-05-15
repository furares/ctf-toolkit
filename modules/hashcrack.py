import subprocess as s
from time import sleep
import os
from termcolor import colored
from datetime import datetime
import hashlib

class hashCrack:

    @staticmethod
    def clear():
        s.run("clear", shell=True)

    @staticmethod
    def get_input(prompt, err_msg="[-] Invalid Input"):
        try:
            return input(prompt)
        
        except (ValueError,KeyboardInterrupt):
            print(colored(f"\n{err_msg}", "red", attrs=['bold']))
            return None
        
    @staticmethod
    def read(wordlist):
        global pass_file
        try:
            pass_file = open(wordlist, "r")
        except:
            print(colored("[!] File Not Found", "red", attrs=['bold']))
            quit()
    @staticmethod
    def hash_found(enter_hash,wordlist):
        
        global word,enc_word,Diget

        if choice == 1:

            hashCrack.read(wordlist)
            for word in pass_file:
                word = word.strip()
                try:
                    enc_word = word.encode("latin-1")
                except UnicodeEncodeError:
                    print(colored("[-] Check Hash Format...", "red", attrs=['bold']))
                    return None
                Diget = hashlib.md5(enc_word).hexdigest()

                if Diget == enter_hash:
                    print(colored(f"[+] Hash Found : {word}", "green", attrs=['bold']))
                    return
                else:
                    pass
        if choice == 2:
            hashCrack.read(wordlist)
            for word in pass_file:
                word = word.strip()
                try:
                    enc_word = word.encode("latin-1")
                except UnicodeEncodeError:
                    print(colored("[-] Check Hash Format...", "red", attrs=['bold']))
                    return None
                Diget = hashlib.sha1(enc_word).hexdigest()

                if Diget == enter_hash:
                    print(colored(f"[+] Hash Found : {word}", "green", attrs=['bold']))
                    return
                else:
                    pass
        
        if choice == 3:

            hashCrack.read(wordlist)
            for word in pass_file:
                word = word.strip()
                try:
                    enc_word = word.encode("latin-1")
                except UnicodeEncodeError:
                    print(colored("[-] Check Hash Format...", "red", attrs=['bold']))
                    return None
                Diget = hashlib.sha256(enc_word).hexdigest()

                if Diget == enter_hash:
                    print(colored(f"[+] Hash Found : {word}", "green", attrs=['bold']))
                    return
                else:
                    pass
        if choice == 4:
            hashCrack.read(wordlist)
            for word in pass_file:
                word = word.strip()
                try:
                    enc_word = word.encode("latin-1")
                except UnicodeEncodeError:
                    print(colored("[-] Hash Not Found !!", "red", attrs=['bold']))
                    return None
                Diget = hashlib.sha512(enc_word).hexdigest()

                if Diget == enter_hash:
                    print(colored(f"[+] Hash Found : {word}", "green", attrs=['bold']))
                    return
                else:
                    pass




    
    
    @staticmethod        
    def crack():

        hashCrack.clear()

        date = colored(datetime.today().strftime('%Y-%m-%d %H:%M'), "red", attrs=['bold'])

        print(f"""
======================================
           HashCracker Tool  
     >>> Developed by Furares <<<
======================================
{date}
{"-"*16}
1- MD5
2- SHA1
3- SHA256
4- SHA512
0- Exit
    """)
        
        global choice

        choice_input = hashCrack.get_input("Enter Process ID => ")

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
            enter_hash = hashCrack.get_input("Enter Hash : ")
            if not enter_hash:
                return
            
            
            wordlist = hashCrack.get_input("Enter Wordlist : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("[!] Wordlist File Not Found", "red", attrs=['bold']))
                pass

            hashCrack.hash_found(enter_hash,wordlist)
            


        if choice == 2:
            enter_hash = hashCrack.get_input("Enter Hash : ")
            if not enter_hash:
                return
            wordlist = hashCrack.get_input("Enter Wordlist : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("File Not Found", "red", attrs=['bold']))
                return
            
            hashCrack.hash_found(enter_hash=enter_hash, wordlist=wordlist)

        if choice == 3:
            enter_hash = hashCrack.get_input("Enter Hash : ")
            if not enter_hash:
                return
            wordlist = hashCrack.get_input("Enter Wordlist : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("File Not Found", "red", attrs=['bold']))
                return
            
            hashCrack.hash_found(enter_hash=enter_hash, wordlist=wordlist)

        if choice == 4:

            enter_hash = hashCrack.get_input("Enter Hash : ")
            if not enter_hash:
                return
            wordlist = hashCrack.get_input("Enter Wordlist : ")
            if not wordlist or not os.path.isfile(wordlist):
                print(colored("File Not Found", "red", attrs=['bold']))
                return
            
            hashCrack.hash_found(enter_hash=enter_hash, wordlist=wordlist)

                    
            
            

