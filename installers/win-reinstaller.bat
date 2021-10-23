@echo off
net session >nul 2>&1 || (echo Run as admin!&pause >nul&goto :eof)
echo Make sure to install 'phoenixminer python3 and git'
cd %APPDATA%
rmdir Phoenix-Assist
git clone https://github.com/MadRoadStudio/Phoenix-Assist
cd Phoenix-Assist\win-bin
copy mine.bat %WINDIR%\system32
copy phoenixassist.bat %WINDIR%\system32
copy phoenix-assist.bat %WINDIR%\system32
echo Reinstalled! Use 'mine' to start.
echo Click any key to continue...
pause >nul
exit