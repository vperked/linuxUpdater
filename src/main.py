import time
from cmd.update import Updater
from cmd.util import MachineUtil

if __name__ == "__main__":
    if MachineUtil.checkRoot():
        answer = input().strip()
        if answer == "updater":
            while True:
                try:
                    Updater.linuxUpdate()
                    time.sleep(3600)
                except KeyboardInterrupt:
                    print("Stopped!")
                    break
                except Exception as e:
                    print(e)