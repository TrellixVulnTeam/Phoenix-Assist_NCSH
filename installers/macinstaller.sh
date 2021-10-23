#!/bin/bash
oldpwd = pwd
echo "Make sure to install 'phoenixminer python3 git and nano' "
cd ~/Library/Preferences/
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist
sudo cp -a mac-bin/* /usr/local/bin/
cd oldpwd
echo "Installed! Use 'mine' to start."
