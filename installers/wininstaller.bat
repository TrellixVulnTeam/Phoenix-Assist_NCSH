@echo off
net session >nul 2>&1 || (echo Run as admin!&pause >nul&goto :eof)
IF EXIST %WINDIR%\system32\mine.bat GOTO :err1
echo Make sure to install 'phoenixminer python3 and git'
cd %APPDATA%
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist\win-bin
copy mine.bat %WINDIR%\system32
copy phoenixassist.bat %WINDIR%\system32
copy phoenix-assist.bat %WINDIR%\system32
echo Installed! Use 'mine' to start.
echo Click any key to continue...
pause >nul
exit
:err1
echo This app is already installed! (error 1)
echo Click any key to continue...
pause >nul
exit