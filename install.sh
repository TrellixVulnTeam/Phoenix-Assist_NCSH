#!/bin/bash
echo "Make sure to install 'phoenixminer python3 git' "
cd ~/Documents
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist/bin
echo "export PATH=$PWD:\$PATH" >> ~/.bashrc
exec $0
echo "Installed! Use 'mine' to start."
