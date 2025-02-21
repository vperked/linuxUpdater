import platform
from colorama import init, Fore, Style
class Logger:
    def __init__(self):
        self.start = False

    def hasRan(self):
        if not self.start:
            self.start = True
            return
        else:
            print("Already ran!")
        print("Already ran!")

    def isRunning(self):
        if self.start:
            print(Fore.RED + f"OS: {platform.system()}, Arch: {platform.machine()}")
        else:
            print("Not running!")