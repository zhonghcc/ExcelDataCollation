@echo off

set base=%cd%
echo %base%
echo "removing temp files"
rd /s /q %base%\dist
rd /s /q %base%\build
pause
pyinstaller -w app.py 
xcopy %base%\resources %base%\dist\app\resources /i /e
xcopy %base%\config %base%\dist\app\config /i /e
mkdir %base%\dist\app\logs
copy logging.conf %base%\dist\app\logging.conf
echo "starting to compress"
7za a app.zip .\dist\*
pause