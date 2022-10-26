@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN='Здесь должен был быть Token'

python telegram_bot.py

pause 
