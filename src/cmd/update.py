import subprocess
class Updater:
    def linuxUpdate():
        try:
            cmd = subprocess.run(["sudo", "apt", "update", "-y"], check=True)
            if cmd.returncode == 0:
                print("Package update grabbed!")
                Updater.linuxUpgrade()
        except Exception as e:
            print(e)
    def linuxUpgrade():
        try: 
            cmd = subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
            print(cmd.stdout)
            print("Complete!")
            return True
        except Exception as e:
            print(e)