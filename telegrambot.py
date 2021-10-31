#!/usr/bin/env python
# coding: utf-8

# PER TROVARE IL TOKEN DEVI DECRIPTARE token.gpg COL COMANDO
# gpg token.gpg
# LA PASSWORD PER DECRIPTARE È IL NOME DEL CONO STRADALE 
# (TUTTO MINUSCOLO, TUTTO UNITO)
bot_token  = 'INSERISCI TOKEN'
bot_chatID = '-1001604234843'

from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests
from datetime import date

from scraping import bs_splitdishes, bs_dishesfindnames, bs_dishesfindtypes, bs_shrinkhtmltodate, bs_gethtml

# The URLs where to take all the informations.
# The first value after menu/ tells the day (in UNIX time)
# The other two are useless
# The last one is 3 for pranzo, 5 for cena
url_pranzo = 'https://donmazza.serenissimacloud.it/menu/'+str(int(time.time()))+'/0/0/3'
url_cena   = 'https://donmazza.serenissimacloud.it/menu/'+str(int(time.time()))+'/0/0/5'

html_pranzo  = bs_splitdishes(bs_shrinkhtmltodate(bs_gethtml(url_pranzo)))
html_cena    = bs_splitdishes(bs_shrinkhtmltodate(bs_gethtml(url_cena)))

names_pranzo = bs_dishesfindnames(html_pranzo)
names_cena   = bs_dishesfindnames(html_cena)

tipi_pranzo  = bs_dishesfindtypes(html_pranzo)
tipi_cena    = bs_dishesfindtypes(html_cena)

def print_message():    
    today = date.today()
    print('Menù del giorno: ', today.strftime("%d/%m/%y"))
    
    print("\nPranzo")
    print("  Primi")
    for i in range(len(html_pranzo)):
        if tipi_pranzo[i] == '1':
            print('    ',names_pranzo[i])
    print("  Secondi")
    for i in range(len(html_pranzo)):
        if tipi_pranzo[i] == '2':
            print('    ',names_pranzo[i])
    print("  Contorni")
    for i in range(len(html_pranzo)):
        if tipi_pranzo[i] == '4':
            print('    ',names_pranzo[i])
    print("\nCena")
    print("  Primi")
    for i in range(len(html_cena)):
        if tipi_cena[i] == '1':
            print('    ',names_cena[i])
    print("  Secondi")
    for i in range(len(html_cena)):
        if tipi_cena[i] == '2':
            print('    ',names_cena[i])
    print("  Contorni")
    for i in range(len(html_cena)):
        if tipi_cena[i] == '4':
            print('    ',names_cena[i])
            
def create_message():  
    today = date.today()
    intro  = 'Menù del giorno: '+str(today.strftime("%d/%m/%y"))
    
    pranzo = '\n\n*Pranzo*\n  *Primi*'
    for i in range(len(html_pranzo)):
        if tipi_pranzo[i] == '1':
            pranzo = pranzo +'\n    '+str(names_pranzo[i])
    pranzo = pranzo + '\n  *Secondi*'
    for i in range(len(html_pranzo)):
        if tipi_pranzo[i] == '2':
            pranzo = pranzo +'\n    '+str(names_pranzo[i])
    pranzo = pranzo + '\n  *Contorni*'
    for i in range(len(html_pranzo)):
        if tipi_pranzo[i] == '4':
            pranzo = pranzo +'\n    '+str(names_pranzo[i])
            
    cena = '\n\n*Cena*\n  *Primi*'
    for i in range(len(html_cena)):
        if tipi_cena[i] == '1':
            cena = cena +'\n    '+str(names_cena[i])
    cena = cena + '\n  *Secondi*'
    for i in range(len(html_cena)):
        if tipi_cena[i] == '2':
            cena = cena +'\n    '+str(names_cena[i])
    cena = cena + '\n  *Contorni*'
    for i in range(len(html_cena)):
        if tipi_cena[i] == '4':
            cena = cena +'\n    '+str(names_cena[i])
    
    message = intro + pranzo + cena
    
    return message

def telegram_bot_sendtext(bot_message):    
    send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message

    response = requests.get(send_text)

    return response.json()

# Send the message iff there's a menu
if html_pranzo:
    telegram_bot_sendtext(create_message())




