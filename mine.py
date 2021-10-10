import os
import json
import time
import platform

with open(os.path.expanduser("~") + '/Documents/Phoenix-Assist/settings.json') as f:
    data = json.load(f)

def oldstyle():
    if data["oldstyle"] == "yes" or "y":
        time.sleep(0.025)

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

    wallet = " -wal 0x" + data["wallet"]
    pool1 = " -pool " + data["pool1"]
    password = ""
    coin = ""
    worker_name = ""
    pool2 = ""
    wallet2 = ""
    parameters = ""

    if data["password"] != "":
        password = " -pass " + data["password"]
    if data["coin"] != "":
        coin = " -coin " + data["coin"]
    if data["worker_name"] != "":
        worker_name = " -worker " + data["worker_name"]
    if data["pool2"] != "":
        pool2 = " -pool2 " + data["pool2"]
    if data["wallet2"] != "":
        wallet2 = " -wallet2 " +  data["wallet2"]
    if data["parameters"] != "":
        parameters = " " + str(data["parameters"])
    if data["log"].lower() == "no" or "n" or "0":
        log = " -log 0"
    elif data["log"].lower() == "yes" or "y" or "1":
        try:
            os.mkdir(os.getcwd() + "/log")
            log = " -log 1 -logdir " + str(os.getcwd()) + "/log"
        except FileExistsError:
            log = " -log 1 -logdir " + str(os.getcwd()) + "/log"
    elif data["log"].lower() == "2" or "show" or "s":
        try:
            os.mkdir(os.getcwd() + "/log")
            log = " -log 2 -logdir " + str(os.getcwd()) + "/log"
        except FileExistsError:
            log = " -log 2 -logdir " + str(os.getcwd()) + "/log"
    else:
        log = " -log 0"
    
    if data["sudo"].lower() == "n" or "no" or "0":
        cmd = str(pm) + str(wallet) + str(pool1) + str(password) + str(coin) + str(worker_name) + str(pool2) + str(wallet2) + str(log) + str(parameters)
    else:
        cmd = "sudo " + str(pm) + str(wallet) + str(pool1) + str(password) + str(coin) + str(worker_name) + str(pool2) + str(wallet2) + str(log) + str(parameters)
        
    os.system("clear")
    print(cmd)
    if data["wallet"] != "":
        print("You need to input a wallet! Check settings to do so.")
    if data["pool1"] != "":
        print("You need to input a pool! Check settings to do so.")
    try:
        print("Running, CTRL+C to quit")
        time.sleep(1)
        os.system(str(cmd))
        print("Phoenix Miner closed")
        input("Press enter to continue...")
        menu()
    except KeyboardInterrupt:
        menu()

def sett():
    os.system("clear")
    os.system("nano " + os.path.expanduser("~") + '/Documents/Phoenix-Assist/settings.json')
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

    os.system("clear")
    print("########")
    print("Phoenix Assist")
    print("########")
    print("")
    print("1: Start")
    print("")
    print("2: Settings")
    print("")
    print("3: Exit")
    print("\nYou need to give a valid number.")
    print("\n########")
    try:
        checkans(str(input("")))
    except KeyboardInterrupt:
        exit()


def menu():
    os.system("clear")
    print("########")
    oldstyle()
    print("Phoenix Assist")
    oldstyle()
    print("########")
    oldstyle()
    print("")
    oldstyle()
    print("1: Start")
    oldstyle()
    print("")
    oldstyle()
    print("2: Settings")
    oldstyle()
    print("")
    oldstyle()
    print("3: Exit")
    oldstyle()
    print("\n########")
    oldstyle()
    try:
        checkans(str(input("")))
    except KeyboardInterrupt:
        exit()
menu()