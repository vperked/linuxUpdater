import time
from util.messages import Messages
from cmd.update import Updater
from cmd.util import MachineUtil
from cmd.install import Install
from cmd.iptables import Iptables
def beginLoop():
      while True:
            Messages.Debug.debug("Come back in 12 hours...(Or dont it does not matter)")
            time.sleep(43200)
            if Updater.Linux.linuxUpdate():
                  continue

if __name__ == "__main__":
            Updater.Linux.linuxUpdate()
            a = input("Install openvpn & other useful packages:")
            Messages.Debug.debug("This will whitelist your IP to port 22!")
            if a == "y":
                  Messages.Debug.debug("Installing OpenVPN & other packages")
                  Install.installOpenVPN()
                  Messages.Debug.debug("Done!")
                  Iptables.whiteListIp()
                  Messages.Debug.debug("IP whitelisted")
                  Messages.Debug.debug("Starting loop")
                  beginLoop()
            elif a == "n":
                  Messages.Debug.debug("Not installing OpenVPN & other packages")
                  a2 = input("Do you want to whitelist your IP to port 22:")
                  if a2 == "y":
                        Iptables.whiteListIp()
                  elif a2 == "n":
                        print("Ok, not whitelisting your IP")
                  Messages.Debug.debug("Starting loop")
                  beginLoop()
        