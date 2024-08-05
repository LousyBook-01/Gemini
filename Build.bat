@echo off
call "Install all imports.bat"
pip install pyinstaller
cls
echo Building Files...
pyinstaller --onefile --icon=gemini_icon.ico "Chat With Gemini 1.5 Flash.py"
pyinstaller --onefile --icon=gemini_icon.ico "Chat With Gemini 1.5 Pro.py"
pyinstaller --onefile --icon=gemini_icon.ico "Chat With Gemini 1.0 Pro.py"
cls
echo Done Build
pause