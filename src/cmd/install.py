import subprocess
from util.messages import Messages
class Install:
    def installOpenVPN():
            try:
                Messages.Debug.debug("Install OpenVPN executed!")
                cmd = subprocess.run(["curl", "-O", "https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh"], capture_output=True, text=True)
                Messages.Debug.debug(cmd.stdout)
                cmd2 = subprocess.run(["chmod", "+x", "openvpn-install.sh"], capture_output=True, text=True)
                Messages.Debug.debug(cmd2.stdout)
                Messages.Debug.debug("Done, starting package installation!")
                Install.installPKG()
            except Exception as e:
                Messages.Errors.error(e)
    def installPKG():
        try:
            cmd = subprocess.run(
         [ "apt", "install", "-y", "nload", "dirmngr", "ca-certificates", "python3", "bpytop", "golang", "python3-pip",
            "build-essential", "net-tools", "dstat", "tcpdump", "iptables-persistent",
            "nmap", "ipset", "conntrack", "sudo"
        ], capture_output=True, text=True)
            if cmd.returncode == 0:
                Messages.Debug(f"Command: {cmd.stdout}")
            else:
                Messages.Errors.error(f"Command: {cmd.stderr}")
        except Exception as e:
            Messages.Errors.error(e)