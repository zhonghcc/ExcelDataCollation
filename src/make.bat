@echo off

set base=%cd%
echo %base%
echo "removing temp files"
rd /s /q %base%\dist
rd /s /q %base%\build
pause
pyinstaller -w app.py 
xcopy %base%\resources %base%\dist\app\resources /i /e
copy logging.conf %base%\dist\app\logging.conf
copy data.db %base%\dist\app\data.db
echo "starting to compress"
7za a app.zip .\dist\*
pause