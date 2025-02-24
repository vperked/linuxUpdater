import os
import sys
import platform
import subprocess
from util.messages import Messages
class MachineUtil:
    def getIp():
        try:
            cmd = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
            if cmd.returncode == 0:
                ips = cmd.stdout.strip().split()
                if ips:
                    Messages.Debug.debug(f"IP address: {ips[0]}")
                    return ips[0]
                else:
                    Messages.Errors.error("No IP address found")
            else:
                Messages.Errors.error("Failed to get IP address")
        except Exception as e:
            Messages.Errors.error(e)
    def checkMachine():
        if platform.system() == "Windows":
            return "win"
        elif platform.system() == "Linux":
            return "lin"

    def checkRoot():
        if os.getuid() == 0:
            print(f"{os.getlogin()} is root!")
            return True
        else:
            print(f"{os.getlogin()} is not root!")
            return False
            