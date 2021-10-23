@echo off
net session >nul 2>&1 || (echo Run as admin!&goto :eof)
IF EXIST %WINDIR%\system32\mine.bat GOTO :do
echo App is not installed!
echo Click any key to continue...
pause >nul
exit
:do
rmdir %APPDATA%\Phoenix-Assist
rm %WINDIR%\system32\mine.bat
rm %WINDIR%\system32\phoenixassist.bat
rm %WINDIR%\system32\phoenix-assist.bat
echo This app has been uninstalled.
echo Click any key to continue...
pause >nul
exit