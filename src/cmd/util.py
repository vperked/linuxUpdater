import os


class MachineUtil:
    def checkRoot():
        if os.getuid() == 0:
            print(f"{os.getlogin()} is root!")
            return True
        else:
            print(f"{os.getlogin()} is not root!")
            return False
    def doesENVExist():
        env = os.environ.get("/dareUpdater/venv")
        if env:
            print("ENV!")
            return True
        else:
            print("None")
            return False