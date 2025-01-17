@echo off

echo Hello! Welcome to the Quiz Master app.

set /p isTrue=<installed.txt

if %isTrue%==0 (
    set isTrue=1
    echo Installing Libs.
    echo Make sure that you installed Python and you are connected to the internet.

    python -m pip install -r requirements.txt

    echo Installation is finished. Enjoy!
)

echo %isTrue% > installed.txt

cd "..\app"
python main.py
pause