import subprocess
from util.messages import Messages
class Updater:
    class Linux:
        def linuxUpdate():
            try:
                cmd = subprocess.run(["sudo", "DEBIAN_FRONTEND=noninteractive", "apt", "update", "-y"], check=True)
                if cmd.returncode == 0:
                    print("Package update grabbed!")
                    Messages.Debug.debug(cmd.stdout)
                    Updater.Linux.linuxUpgrade()
            except Exception as e:
                Messages.Error.error(e)
        def linuxUpgrade():
            try: 
                cmd = subprocess.run(["apt", "upgrade", "-y"], check=True)
                Messages.Debug.debug(cmd.stdout)
                return True
            except Exception as e:
                Messages.Error.error(e)