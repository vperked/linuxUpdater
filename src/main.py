import time
from cmd.update import Updater
from cmd.util import MachineUtil
from cmd.logger import Logger

logger = Logger()
if __name__ == "__main__":
    if MachineUtil.checkRoot():
        logger.hasRan()
        logger.isRunning()
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