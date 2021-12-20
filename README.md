# Telegram Bot to deliver daily the menu at Collegio Universitario D. Nicola Mazza

## Installation on NASSUZ
 -TODO

## Installation on a Linux Machine (with Python)
 1. Insert the Bot Token in `telegrambot.py`
 2. Add `telegrambot.py` on crontab:
   * `crontab -e`
   * `8 0 * * *  python path/to/telegrambot.py`  

## Installation on a Windows machine
 1. Insert the Bot Token in `telegrambot.py`
 2. Run `scheduler.bat` as automated task in Task Scheduler (check in `scheduler.bat` if paths are still correct)
