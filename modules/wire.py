import subprocess as s
from time import sleep

class wireshark:
    @staticmethod
    def start():
        s.run("sudo wireshark", shell=True)
        
        