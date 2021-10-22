echo off
net session >nul 2>&1 || (echo Run as admin!&goto :eof)
echo Make sure to install 'phoenixminer python3 and git'
cd %APPDATA%
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist\win-bin
copy mine.bat %WINDIR%\system32
copy phoenixassist.bat %WINDIR%\system32
copy phoenix-assist.bat %WINDIR%\system32
echo "Installed! Use 'mine' to start."	