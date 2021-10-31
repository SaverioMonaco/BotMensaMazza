from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests
from datetime import date


def bs_gethtml(url):
    # request to site, most probably it still is: https://donmazza.serenissimacloud.it
    page = requests.get(url)
    soup = str(BeautifulSoup(page.text)) # get the string
    
    return soup

def bs_shrinkhtmltodate(page_html):
    today = date.today()
    
    giorno = '20'+today.strftime("%y")+'-'+today.strftime("%m")+'-'+today.strftime("%d") # to be updated in 80 years
    
    starting_index = page_html.find('!-- INIZIO Piatti del giorno '+giorno+' -->')
    ending_index   = page_html.find('!-- FINE Piatti del giorno '+giorno+' -->')
    
    return page_html[starting_index:ending_index]

def bs_splitdishes(page_html):
    dishes = []
    keyword = 'cbp-item cbp-l-grid-masonry-projects'
    endword = 'cbp-l-grid-masonry-projects-desc'
    for i in range(len(page_html)):
        #print(i)
        if page_html[i:i+len(keyword)] == keyword:
            starting_index = i
            j = i
            found = False
            while not found:
                if page_html[j:j+len(endword)] == endword:
                    ending_index = j
                    found = True
                    dishes.append(page_html[starting_index:ending_index])
                j = j + 1
    
    return dishes

def bs_dishesfindnames(dishes):
    keyword = '"cbp-l-grid-masonry-projects-title">'
    endword = '</div>'
    
    names = []
    shift = len(keyword)
    for dish in range(len(dishes)):
        dish_code = dishes[dish]
        for i in range(len(dish_code)):
            if dish_code[i:i+len(keyword)] == keyword:
                starting_index = i
                j = i
                found = False
                while not found:
                    if dish_code[j:j+len(endword)] == endword:
                        ending_index = j
                        found = True
                        names.append(dish_code[starting_index + shift:ending_index])
                    j = j + 1
                    
    return names

def bs_dishesfindtypes(dishes):
    types = []
    for dish in range(len(dishes)):
        types.append(dishes[dish][40:41])
    
    return types