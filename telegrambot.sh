#!/bin/sh

# PER TROVARE IL TOKEN DEVI DECRIPTARE token.gpg COL COMANDO
# gpg token.gpg
# LA PASSWORD PER DECRIPTARE È IL NOME DEL CONO STRADALE
# (TUTTO MINUSCOLO, TUTTO UNITO)
bot_token='INSERT_TOKEN'
bot_chatID='-1001604234843'

# The URLs where to take all the informations.
# The first value after menu/ tells the day (in UNIX time)
# The other two are useless
# The last one is 3 for pranzo, 5 for cena
url="https://donmazza.serenissimacloud.it/menu/$(date +'%s')/0/0/"

print_dish() {
  echo "  *$2*"
  echo "$3" \
    | grep -ohE "cbp-item[ \\t]+cbp-l-grid-masonry-projects[ \\t]+dt_$1[^>]*>([ \\t]*<[^>]+>|VISUALIZZA)*([^<]+)" \
    | sed 's/.*>\([^>]*\)$/    \1/'
}

get_menu() {
  echo -e "\n*$2*"
  html="$(curl -k "$url$1" | tr '\n' ' ' \
    | grep -oh "<!-- INIZIO Piatti del giorno.*<!-- FINE Piatti del giorno")"
  print_dish 1 Primi "$html"
  print_dish 2 Secondi "$html"
  print_dish 4 Contorni "$html"
}

message="Menù del giorno: $(date +'%d/%m/%Y')
$(get_menu 3 Pranzo)
$(get_menu 5 Cena)"

if [ ${#message} -gt 400 ]
then
  curl \
    --data "chat_id=$bot_chatID" \
    --data "parse_mode=Markdown" \
    --data-urlencode "text=$message" \
    "https://api.telegram.org/bot$bot_token/sendMessage"
fi

