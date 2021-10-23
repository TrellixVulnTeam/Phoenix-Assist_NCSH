#!/bin/bash
oldpwd = pwd
cd ~/.local/share/
rmdir Phoenix-Assist
rm /usr/bin/mine
rm /usr/bin/phoenixassist
rm /usr/bin/phoenix-assist
cd oldpwd
echo "Uninstalled"
