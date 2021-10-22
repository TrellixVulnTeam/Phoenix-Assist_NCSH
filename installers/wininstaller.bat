echo "Make sure to install 'phoenixminer python3 and git' "
cd %AppData%
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist
runas /user:Administrator "copy win-bin/* %PATH%"
echo "Installed! Use 'mine' to start."
