# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "http://www.nhltradetracker.com/user/trade_list_by_season/2016-17/1"

fichier = "meilleurbuteurlnh.csv"

entetes = {
    "User-Agent" : "Véronique Senecal",
    "From": "vero.senecal1993@gmail.com"
}

req = requests.get(url,headers=entetes)
# print(req)

page = BeautifulSoup(req.text,"html.parser")
# print(page)

for ligne in page.find("table", class_="s_list").find_all("a"):
    # print(ligne)
    annee = ligne["href"]
    # print(annee[27:34])
    annee = annee[27:34]
    lien = "http://www.nhltradetracker.com/user/trade_list_by_season/{}/1".format(annee)
    print(lien)

for trade in page.find_all("td", class_="label"):
    if "Montreal Canadiens acquire"
    print(span, class_="link".text)
    
# Après avoir trouvé les liens qui menaient aux différentes années des échanges de la LNH, je désirais trouver spécifiquement 
# certains échanges de certaines équipes à un moment X. Malheureusement, je n'ai pas trouvé la formule à utiliser afin de réussir 
# mon objectif. Je croyais que la même formule que la précédente pouvait fonctionner une seconde fois en changeant les valeurs. 
