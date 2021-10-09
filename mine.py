import os
import json
import time
import platform
with open('settings.json') as f:
    data = json.load(f)
#example print(sett[required.wallet])
def oldstyle():
    if data["oldstyle"] == "yes":
        time.sleep(0.05)

def start():
    pm_path = data["pm_path"]
    if platform.system() == "Windows":
        pm = data["pm_windows"]
    elif platform.system() == "Linux":
        if pm_path == "":
            pm = data["pm_linux1"]
        else:
            pm = data["pm_linux2"]
    elif platform.system() == "Darwin":
        print("macOS isn't fully supported. You may encounter some bugs.")
        if pm_path == "":
            pm = data["pm_linux1"]
        else:
            pm = data["pm_linux2"]
    else:
        print(platform.system() + " isn't fully supported. You may encounter some bugs.")
        if pm_path == "":
            pm = data["pm_linux1"]
        else:
            pm = data["pm_linux2"]

    wallet = "-wallet", data["wallet"]
    pool1 = " -pool", data["pool1"]
    password = ""
    coin = ""
    worker_name = ""
    pool2 = ""
    wallet2 = ""
    parameters = ""

    if data["password"] != "":
        password = " -p", data["password"]
    if data["coin"] != "":
        coin = " -coin", data["coin"]
    if data["worker_name"] != "":
        worker_name = " -worker", data["worker_name"]
    if data["pool2"] != "":
        pool2 = " -pool2", data["pool2"]
    if data["wallet2"] != "":
        wallet2 = " -wallet2", data["wallet2"]
    if data["parameters"] != "":
        parameters = data["parameters"]

    cmd = pm, wallet + pool1 + password + coin + worker_name + pool2 + wallet2 + parameters
    os.system("clear")
    print(pm)
    try:
        print("Running ")
        os.system(str(cmd))
        print("Phoenix Miner closed or crashed")
        input("Press enter to continue...")
        menu()
    except KeyboardInterrupt:
        menu()

def sett():
    os.system("clear")
    print("Not done yet!")
    time.sleep(1)
    menu()

def quit():
    os.system("clear")
    exit()

def checkans(num):
    if num == "1":
        start()
    elif num == "2":
        sett()
    elif num == "3":
        quit()
    else:
        os.system("clear")
        print("You need to give a valid number.")
        print("# 1: Start")
        print("# 2: Settings")
        print("# 3: Exit")
        checkans(input(""))


def menu():
    os.system("clear")
    print("########\n#")
    oldstyle()
    print("# Phoenix Assist")
    oldstyle()
    print("#\n#######")
    oldstyle()
    print("#")
    oldstyle()
    print("# 1: Start")
    oldstyle()
    print("#")
    oldstyle()
    print("# 2: Settings")
    oldstyle()
    print("#")
    oldstyle()
    print("# 3: Exit")
    oldstyle()
    print("#\n########")
    oldstyle()
    try:
        checkans(str(input("")))
    except KeyboardInterrupt:
        exit()
menu()