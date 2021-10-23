#!/bin/bash
oldpwd = pwd
cd ~/Library/Preferences/
rmdir Phoenix-Assist
rm /usr/bin/mine
rm /usr/bin/phoenixassist
rm /usr/bin/phoenix-assist
cd oldpwd
echo "Uninstalled"
