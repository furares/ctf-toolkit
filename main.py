#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as s
from time import sleep
from modules.nmap import nmaptool
from modules.gobuster import gobusterScan
from modules.hash import hashGen
from modules.hashcrack import hashCrack
from modules.hydra import bruteforce
from modules.rsa import crack_rsa
from modules.met import metasploit
from modules.bet import bettercap
from modules.wire import wireshark
from modules.mac_changer import macchange
from termcolor import colored
from datetime import datetime



def clear():
    s.run("clear", shell=True)

def ask_continue():
    while True:
        try:
            ask = input(colored("Do You Want To Return To The Main Menu? Y/n : ", "cyan", attrs=['bold']))
            if not ask:
                main()
                break
            if ask.lower() == "y":
                main()
            if ask.lower() == "n":
                break
            else:
                break
        except KeyboardInterrupt:
            break
        except EOFError:
            print("\n")
            break
        



def main():

    
    while True:

    
        clear()

        date = colored(datetime.today().strftime('%Y-%m-%d %H:%M'), "green", attrs=['bold'])

        string = colored("Some Tools Need Root. If You Get An Error, Run As Root", "white", "on_red", attrs=['bold'])


        
        print(colored(rf"""
 _____                                                                   _____ 
( ___ )                                                                 ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                   |   | 
 |   |  ______    _____ _   _ ____      _    ____  _____ ____     ______ |   | 
 |   |  \ \ \ \  |  ___| | | |  _ \    / \  |  _ \| ____/ ___|   / / / / |   | 
 |   |   \ \ \ \ | |_  | | | | |_) |  / _ \ | |_) |  _| \___ \  / / / /  |   | 
 |   |   / / / / |  _| | |_| |  _ <  / ___ \|  _ <| |___ ___) | \ \ \ \  |   | 
 |   |  /_/_/_/  |_|    \___/|_| \_\/_/   \_\_| \_\_____|____/   \_\_\_\ |   | 
 |   |                                                                   |   | 
 |   |         Developed By Furares For CTF And Ethical Hacking          |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                 (_____)

Date : {date}""", "blue", attrs=['bold']))
        print(f"""
{string}
              
1- Nmap Scan (Basic Target Scan)
2- Gobuster (Basic Directory/Wordlist Scan)
3- Hash Generator (Generate Hash From Password)
4- Hash Cracker (Crack MD5,SHA1,SHA256,SHA512 Hashes)
5- Password Attack (SSH,FTP BruteForce)
6- RSA Key Cracker (Crack RSA Private Keys)
7- Metasploit (Start Metasploit)
8- Bettercap (Network Sniffing and Spoofing)
9- Wireshark (Analyze Network Traffic)
10- Mac Address Changer (Tested on Linux Mint And Kali Linux)
0- Exit
""")

        try:
            option = int(input("Enter Choice > "))
        except KeyboardInterrupt:
            print(colored("\nGoodbye...", "green", attrs=['bold']))
            break
        except Exception as e:
            print(f"[-] Error: {e}")
            break

        if option == 0:
            print(colored("Goodbye...", "green", attrs=['bold']))
            break


        
        if option == 1:
            clear()
            choice = nmaptool.menu()
            nmaptool.scan(choice)
            ask_continue()
            break
            
            
        elif option == 2:
            clear()
            choice = gobusterScan.main_menu()
            ask_continue()
            break

        elif option == 3:
            choice = hashGen.hashed()
            ask_continue()
            break
        elif option == 4:
            choice = hashCrack.crack()
            ask_continue()
            break
        elif option == 5:
            choice = bruteforce.crack()
            ask_continue()
            break
        elif option == 6:
            clear()
            print(colored("To Use This Tool, The ssh2john Tool Must Be Located In This Directory", "white", "on_red", attrs=['bold']))
            choice = crack_rsa.crack()
            ask_continue()
            break

        elif option == 7:
            metasploit.start()
            ask_continue()
            break

        elif option == 8:
            clear()
            bettercap.start()
            ask_continue()
            break

        elif option == 9:
            clear()
            wireshark.start()
            ask_continue()
            break

        elif option == 10:
            macchange.start()
            ask_continue()
            break
        
        else:
            print(colored("[!] Goodbye...", "green", attrs=['bold']))
            break


if __name__ == "__main__":
    main()


    
