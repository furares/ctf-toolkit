#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as s
from time import sleep
from termcolor import colored
import re
from datetime import datetime
import os
import sys
import random

class macchange:

    @staticmethod
    def check_root():
        if os.geteuid() != 0:
            macchange.clear()
            print(colored("Root privileges are required to perform this operation", "white", "on_red", attrs=['bold']))
            sys.exit(1)


    @staticmethod
    def clear():
        s.run("clear", shell=True)

    @staticmethod
    def menu():
        macchange.clear()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        print(colored(rf"""
*************************************************
*  _____ _   _ ____      _    ____  _____ ____  *
* |  ___| | | |  _ \    / \  |  _ \| ____/ ___| *
* | |_  | | | | |_) |  / _ \ | |_) |  _| \___ \ *
* |  _| | |_| |  _ <  / ___ \|  _ <| |___ ___) |*
* |_|    \___/|_| \_\/_/   \_\_| \_\_____|____/ *
*              Mac Address Changer              *
*************************************************
{colored(now, "green", attrs=['bold'])}
""", "blue", attrs=['bold']))

    @staticmethod    
    def start():

        macchange.check_root()
        while True:
                macchange.menu()
                charlist = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #Char For New Mac Address
                newmac = ":".join(''.join(random.choice(charlist) for _ in range(2)) for _ in range(6))
                   

                print(colored("[+] New Mac Address Is Preparing...", "green", attrs=['bold']))
                sleep(0.5)

                try:
                    interface = input(colored("Enter Network Interface : ", "green", attrs=['bold']))
                except KeyboardInterrupt:
                    print(colored("\nGoodbye...", "green", attrs=['bold']))
                    return
                except ValueError:
                    print(colored("[-] Invalid Input", "red", attrs=['bold']))
                    return
                except Exception as e:
                    print(colored(f"[-] Error Occurred : {e}", "red", attrs=['bold']))
                    return
                
                if not interface or not re.match(r'^[a-zA-Z0-9]+$', interface):
                    print(colored("[-] Invalid Interface Name", "red", attrs=['bold']))
                    return


                try:
                    ifconfig = s.check_output(['ifconfig', interface]).decode()
                except s.CalledProcessError:
                    print(colored(f"[-] Interface {interface} not found", "red", attrs=['bold']))
                    return

                oldmac_match = re.search(r"ether\s+([0-9a-fA-F:]{17})", ifconfig)
                if oldmac_match:
                    oldmac = oldmac_match.group(1)
                else:
                    print(colored("[-] MAC address could not be found in ifconfig output", "red", attrs=["bold"]))
                    return

                
                try:
                    s.check_output(['ifconfig', interface, 'down'])
                    print(colored("[+] Connection Down...", "green", attrs=['bold']))
                    sleep(4)
                    s.check_output(['ifconfig', interface, 'hw', 'ether',newmac])
                    print(colored("[+] Changing Mac Address...", "green", attrs=['bold']))
                    sleep(1)
                    s.check_output(['ifconfig', interface, 'up'])
                    print(colored("[+] Reconnecting To Network", "green", attrs=['bold']))
                    sleep(2)
                    break
                except s.CalledProcessError:
                    continue


        print(colored(f"""
[+] Your Mac Address Changed Successfully
[*] Old Mac Address :  {oldmac}
[*] New Mac Address : {newmac}           
        """, "magenta", attrs=['bold']))


