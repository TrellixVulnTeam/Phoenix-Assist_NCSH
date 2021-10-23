#!/bin/bash
echo "Make sure to install 'phoenixminer python3 git and nano' "
cd ~/.local/share/
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist
sudo cp -a linux-bin/* /usr/bin/
echo "Installed! Use 'mine' to start."
