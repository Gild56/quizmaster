@echo off

echo Uninstalling Quiz Master App.
echo Make sure to click on the Uninstall button.

cd ../../../../command/

dir python-64bit.exe

if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    python-64bit.exe
) else (
    python-32bit.exe
)

cd ../../
rd /s /q "quizmaster"
