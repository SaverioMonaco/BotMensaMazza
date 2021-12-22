# Telegram Bot to deliver daily the menu at Collegio Universitario D. Nicola Mazza

## Installation on NASSUZ
 1. From the web interface package manager assure Perl is installed.
 2. copy the files `perl` and `telegrambot.pl` in  `/share/access_bot/botmensamazza`
 3. Insert the Bot Token in `telegrambot.pl`
 4. Add `telegrambot.pl` on crontab:
   * Add to the file `/etc/config/crontab` the line: `0 8 * * * /share/access_bot/botmensamazza/perl /share/access_bot/botmensamazza/telegrambot.pl`
   * `/etc/config/crontab && /etc/init.d/crond.sh restart`  
   IMPORTANT: do not run `crontab -e`

## Installation on a Linux Machine (with Python)
 1. Insert the Bot Token in `telegrambot.py`
 2. Add `telegrambot.py` on crontab:
   * `crontab -e`
   * `0 8 * * *  python path/to/telegrambot.py`  

## Installation on a Windows machine
 1. Insert the Bot Token in `telegrambot.py`
 2. Run `scheduler.bat` as automated task in Task Scheduler (check in `scheduler.bat` if paths are still correct)
