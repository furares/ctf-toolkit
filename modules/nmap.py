#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess as s
from time import sleep
from termcolor import colored

class nmaptool:

    @staticmethod
    def menu():
        print(f"""
=============================================================
1- Nmap <target>
2- Nmap -sV -sC -A <target>
3- Nmap -sS -sC -sV -T4 -O -oN <file_name> <target>
4- Nmap -sU -sC -sV -O -oN <file_name> <target> {colored("<Recommended>", "white", "on_red", attrs=['bold'])}
5- Nmap -sS -sC -A -p- <target>
6- Nmap -sS -sC -A -p- -oN <file_name> <target> {colored("<Recommended>", "white", "on_red", attrs=['bold'])}
7- Nmap -sS -sC -sV -p- <target>
8- Nmap -sS -sC -sV -p <port> -oN <file_name> <target>
9- Nmap -sS -sC -sV -p <port> -O -oN <file_name> <target>
10-Nmap -sS -sC -sV -O -oN <file_name> <target> {colored("<Recommended>", "white", "on_red", attrs=['bold'])}
0- Exit
=============================================================
        """)
        try:
            return int(input("Enter Process ID => "))
        except ValueError:
            print(colored("[-] Invalid Input, Please Enter A Number.", "red", attrs=['bold']))
            return None
        except KeyboardInterrupt:
            print(colored("\n[-] Goodbye...", "red", attrs=['bold']))
        except Exception as e:
            print(colored(f"[-] Unexpected error: {e}", "red", attrs=['bold']))
            return None

    @staticmethod
    def clear():
        s.run("clear", shell=True)

    def file_name():
        try:
            global file_names
            file_names = input("Enter File Name : ")
        except ValueError:
            print(colored("[-] Inavlid Input", "red", attrs=['bold']))
            return
        except KeyboardInterrupt:
            print(colored("\nGoodbye", "green", attrs=['bold']))
            return
    
    
    
    @staticmethod
    def warning():
        print(colored("\n[+]File saved in nmap_output", "red", attrs=['bold']))    
    
    
    @staticmethod
    def scan(choice):
        if choice is None:
            print("[-] Scan aborted due to invalid input.")
            return

        if choice == 0:
            print(colored("[!] Thanks for using...", "green", attrs=['bold']))
            sleep(0.5)
            return

        try:
            target = input("Enter Target Host : ")
        except ValueError:
            print(colored("[-] Invalid Input", "red", attrs=['bold']))
            return
        except KeyboardInterrupt:
            print(colored("\nGoodbye...", "green", attrs=['bold']))

        if choice == 1:
            nmaptool.clear()
            s.run(["sudo", "nmap", target])
        elif choice == 2:
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sV", "-sC", "-A", target])
        elif choice == 3:
            nmaptool.file_name()
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-sV", "-T4", "-O", "-oN", f"nmap_output/{file_names}", target])
            nmaptool.warning()
        elif choice == 4:
            nmaptool.file_name()
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sU", "-sC", "-sV", "-O", "-oN", f"nmap_output/{file_names}", target])
            nmaptool.warning()
        elif choice == 5:
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-A", "-p-", target])
        elif choice == 6:
            nmaptool.file_name()
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-A", "-p-", "-oN", f"nmap_output/{file_names}", target])
            nmaptool.warning()
        elif choice == 7:
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-sV", "-p-", target])
        elif choice == 8:
            port = input("Enter Port : ")
            nmaptool.file_name()
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-sV", "-p", port, "-oN", f"nmap_output/{file_names}", target])
            nmaptool.warning()
        elif choice == 9:
            port = input("Enter Port : ")
            nmaptool.file_name()
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-sV", "-p", port, "-O", "-oN", f"{file_names}", target])
            nmaptool.warning()
        
        elif choice == 10:
            nmaptool.file_name()
            nmaptool.clear()
            s.run(["sudo", "nmap", "-sS", "-sC", "-sV", "-oN", f"nmap_output/{file_names}", target])
            nmaptool.warning()

        else:
            nmaptool.clear()
            print(colored("[-] Invalid choice", "red"))
