import subprocess
class Updater:
    def pipUpgrade():
        try:
            cmd = subprocess.run(["pip", "install", "--upgrade", "pip"], check=True)
            if cmd.returncode == 0:
                print("Pip upgrade grabbed!")
        except Exception as e:
            print(e)
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
            Updater.pipUpgrade()
        except Exception as e:
            print(e)