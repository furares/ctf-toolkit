import subprocess as s
from time import sleep
from termcolor import colored

class vpn:

    @staticmethod
    def get_input(prompt, err_msg="[-] Invalid Input"):
        try:
            return input(prompt)
        except (ValueError, KeyboardInterrupt, FileExistsError):
            print(colored(f"\n{err_msg}", "red", attrs=['bold']))
            return None 
    
    @staticmethod
    def start():
        file_path = vpn.get_input("OpenVpn File Path : ")
        if file_path is None:
            return None
        else:
            s.run(['sudo', 'openvpn', file_path])
