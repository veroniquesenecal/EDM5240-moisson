### MES COMMENTAIRES ET CORRECTIONS SONT MARQUÉS PAR TROIS DIÈSES

### Très intéressant site, que je ne connaissais pas
### Si j'ai bien compris, tu souhaitais moissonner tous les échanges impliquant le Canadien?

### Voici, en fait, une solution pour moissonner tout le contenu depuis 100 ans que contient ce site

# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

### Pas nécessaire de préciser un URL de départ, ici, puisque la structure de tous les URLs est semblable
# url = "http://www.nhltradetracker.com/user/trade_list_by_season/2016-17/1" 

fichier = "transactionsLNH-JHR.csv" ### J'ai renommé le fichier

entetes = {
    "User-Agent" : "Véronique Senecal",
    "From": "vero.senecal1993@gmail.com"
}

### Voici une boucle pour aller chercher toutes les pages de ce site
### Une première pour toutes les saisons possibles
for annee in range(1918,2017):

    ### Puis une autre pour faire toutes les pages possibles à l'intérieur de chaque saison
    for p in range(1,8): ### Je sais, pour les avoir toutes testées, que 8 est le nombre maximum de pages possibles pour une saison
        an1 = str(annee)
        an2 = str(annee+1)[2:]
        saison = "{}/{}".format(an1,an2)
        page = str(p)

        url = "http://www.nhltradetracker.com/user/trade_list_by_season/{}-{}/{}".format(an1,an2,page)

        req = requests.get(url,headers=entetes)
        print(url)
        page = BeautifulSoup(req.text,"html.parser")

### Je teste d'abord quelque chose
### Si la page contient un message d'erreur, je ne la prends pas et je sors de la boucle (avec la commande «break»)
        if page.find("p", class_="error"):
            print("Cette page n'existe pas")
            break

### Sinon (si je n'ai pas de message d'erreur), cela veut dire que la page où je suis rendu existe et j'en ramasse le contenu
        else:
            print("Yé")

### Dans chaque page, les échanges sont contenus dans une balise <table>
### On les prend tous et on fait une boucle dans laquelle on va passer un échange à la fois (en mettant chacun dans la variable «echange») 
            for echange in page.find_all("table", style="border:1px solid #666666; margin-top:5px;"):
                ### On se crée une liste dans laquelle on va mettre toutes les infos pertinentes
                transaction = []

                ### Dans chaque échange, les informations pertinentes se trouvent dans des <td>
                ### Je les prends tous et les mets dans une liste que j'ai appelée «blocs»
                blocs = echange.find_all("td")

                # print(len(blocs))
                # for n in range(0,10):
                #     print(n, blocs[n].text.strip())

                ### Les infos intéressantes sont contenues dans les «blocs» suivants
                date = blocs[6].text.strip()

                equipe1 = blocs[0].text.strip()
                equipe1 = equipe1[:-8] ### Pour enlever le mot « acquires»

                acquisition1 = blocs[3].text.strip()

                equipe2 = blocs[2].text.strip()
                equipe2 = equipe2[:-8]### Pour enlever le mot « acquires»

                acquisition2 = blocs[7].text.strip()

                ### Je mets le tout dans ma liste «transaction»
                transaction = [saison,date,equipe1,acquisition1,equipe2,acquisition2]
                print(transaction)

                ### Et je mets ces infos dans mon fichier CSV
                pk = open(fichier,"a")
                subban = csv.writer(pk)
                subban.writerow(transaction)

                ### Et c'est pas plus compliqué que ça! :)

# for ligne in page.find("table", class_="s_list").find_all("a"):
#     # print(ligne)
#     annee = ligne["href"]
#     # print(annee[27:34])
#     annee = annee[27:34]
#     lien = "http://www.nhltradetracker.com/user/trade_list_by_season/{}/1".format(annee)
#     print(lien)

# for trade in page.find_all("td", class_="label"):
#     if "Montreal Canadiens acquire"
#     print(span, class_="link".text)
    
# # Après avoir trouvé les liens qui menaient aux différentes années des échanges de la LNH, je désirais trouver spécifiquement 
# # certains échanges de certaines équipes à un moment X. Malheureusement, je n'ai pas trouvé la formule à utiliser afin de réussir 
# # mon objectif. Je croyais que la même formule que la précédente pouvait fonctionner une seconde fois en changeant les valeurs. 
