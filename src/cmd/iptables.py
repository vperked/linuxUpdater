import subprocess
from util.messages import Messages
from cmd.util import MachineUtil
class Iptables:
    def whiteListIp():
        ip = MachineUtil.getIp()
        try:
            cmd = subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "-s", ip, "--dport", "22", "-j", "ACCEPT"])
            if cmd.returncode == 0:
                Messages.Debug.debug("IP whitelisted")
            else:
                print("IP not whitelisted")
        except Exception as e:
            Messages.Errors.error(e)