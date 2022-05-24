# Telegram Bot to deliver daily the menu at Collegio Universitario D. Nicola Mazza

## Installation on NASSUZ
 1. Copy the file `telegrambot.sh` in `/share/access_bot/botmensamazza`
 2. Insert the Bot Token in `telegrambot.sh`
 4. Add `telegrambot.sh` on crontab:
   * Add to the file `/etc/config/crontab` the line: `0 8 * * * /share/access_bot/botmensamazza/telegrambot.sh`
   * `crontab /etc/config/crontab && /etc/init.d/crond.sh restart`  
   IMPORTANT: do not run `crontab -e`

## Installation on a Linux Machine (with Python)
 1. Insert the Bot Token in `telegrambot.py`
 2. Add `telegrambot.py` on crontab:
   * `crontab -e`
   * `0 8 * * *  python path/to/telegrambot.py`  

## Installation on a Windows machine
 1. Insert the Bot Token in `telegrambot.py`
 2. Run `scheduler.bat` as automated task in Task Scheduler (check in `scheduler.bat` if paths are still correct)
