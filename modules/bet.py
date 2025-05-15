import subprocess as s
from time import sleep
from termcolor import colored


class bettercap:

    @staticmethod
    def start():

        print(colored("Bettercap Starting...", "green", attrs=['bold']))
        sleep(1)
        s.run("clear", shell=True)
        s.run("sudo bettercap", shell=True)
        