import os
import json
import time
import sys
import subprocess
import platform
import os.path

if platform.system() == 'Darwin':       # macOS
    pwdt = os.path.expanduser("~") + '/Library/Preferences/Phoenix-Assist/settings.json'
elif platform.system() == 'Windows':    # Windows
    pwdt = os.getenv('APPDATA') + '\\Phoenix-Assist\\settings.json'
else:                                   # linux variants
    pwdt = os.path.expanduser("~") + '/.local/share/Phoenix-Assist/settings.json'

with open(pwdt) as f:
    data = json.load(f)

def oldstyle():
    if data["oldstyle"] == "yes" or "y":
        time.sleep(0.025)

def clr():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

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

    wallet = " -wal " + data["wallet"]
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
        
    clr()
    print(cmd)
    try:
        if data["wallet"] == "":
            print("You need to input a wallet! Check settings to do so.")
            time.sleep(2.5)
            menu()
        if data["pool1"] == "":
            print("You need to input a pool! Check settings to do so.")
            time.sleep(2.5)
            menu()
        try:
            subprocess.call([pm, "-v"])
        except FileNotFoundError:
            print("Command", pm, "does not exist! Is Phoenix Miner installed?")
            input("Press enter to continue...")
            menu() 
        print("Running, CTRL+C to quit")
        time.sleep(1) 
        os.system(str(cmd))
        print("Phoenix Miner closed")
        try:
            if sys.argv[1] == "start":
                quit()
        except IndexError:
            pass
        input("Press enter to continue...")
        menu()
    except KeyboardInterrupt:
        menu()

def sett():
    clr()
    try:
        #legacy = os.system("nano " + os.path.expanduser("~") + '/Documents/Phoenix-Assist/settings.json')
        if platform.system() == 'Darwin':       # macOS
            try:
                subprocess.Popen(["nano", "-h"])
                clr()
            except FileNotFoundError:
                print("Command Nano does not exist! Is Nano installed?")
                input("Press enter to continue...")
                menu()  
            pwdt = "nano " + os.path.expanduser("~") + '/Library/Preferences/Phoenix-Assist/settings.json'
            pwd = os.path.expanduser("~") + '/Library/Preferences/Phoenix-Assist/settings.json'
        elif platform.system() == 'Windows':    # Windows
            pwdt = os.getenv('APPDATA') + '\\Phoenix-Assist\\settings.json'
            pwd = os.getenv('APPDATA') + '\\Phoenix-Assist\\settings.json'
        else:                                   # linux variants
            try:
                subprocess.Popen(["nano", "-h"])
                clr()
            except FileNotFoundError:
                print("Command Nano does not exist! Is Nano installed?")
                input("Press enter to continue...")
                menu()  
            pwdt = "nano " + os.path.expanduser("~") + '/.local/share/Phoenix-Assist/settings.json'
            pwd = os.path.expanduser("~") + '/.local/share/Phoenix-Assist/settings.json'

        os.system(pwdt)

        with open(pwd) as f:
            data = json.load(f)
    except KeyboardInterrupt:
        try:
            if sys.argv[1] == "sett":
                quit()
        except IndexError:
            menu()
        menu()
    try:
        if sys.argv[1] == "sett":
            quit()
    except IndexError:
        menu()
    menu()

def quit():
    clr()
    exit()

def checkans(num):
    if num == "1":
        start()
    elif num == "2":
        sett()
    elif num == "3":
        quit()
    else:
        clr()

    clr()
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
    try:
        if sys.argv[1] == "start":
            start()
        elif sys.argv[1] == "sett":
            sett()
    except IndexError:
        pass
    clr()
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