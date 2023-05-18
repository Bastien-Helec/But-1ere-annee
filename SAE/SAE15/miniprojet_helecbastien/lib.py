#module lib
# Copyright © Helec Bastien 
#Version 0.0.1
#2023-01-09
import math
import requests 
from lxml import etree 
from time import sleep
import datetime
import json
# Instant de la mesure (H)
T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Série 1 : températures ( °C )
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]

# Série 2 : températures ( °C )
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]

def moyenne(L):
    """ Calcule la moyenne des valeurs d'une liste"""
    global somme, moyennes
    somme = 0
    moyennes = 0
    for i in range(len(L)):
        somme = somme + L[i]
        moyennes=somme/len(L)
    print(moyennes)


def ecart_alamoyenne(L):
    """ Calcule l'écart à la moyenne des valeurs d'une liste"""
    moyenne(L)
    global alamoy,ecl
    ecl=[]
    alamoy = 0
    for i in range(len(L)):
        ecart=L[i]-moyennes
        ecl.append(ecart)
    print(ecl)

# ecart_alamoyenne(L2)

def mise_au_carré(L):
    """ Calcule la mise au carré des valeurs d'une liste"""
    ecart_alamoyenne(L)
    global carre
    carre=[]
    for i in range(len(ecl)):
        expo=ecl[i]*ecl[i]
        carre.append(expo)
    print(carre)
# mise_au_carré(L1)

def ecart_type(L):
    """ Calcule l'écart type des valeurs d'une liste"""
    mise_au_carré(L)
    sommes=0
    moyennelst=0
    ect=0
    for j in range(len(carre)):
        sommes= sommes + carre[j]
    moyennelst=sommes/len(carre)
    ect=math.sqrt(moyennelst)
        
    print(ect)

def donneesparkings(parkings):
    for i in range(len(parkings)):
        response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml")

        # print(response.text)
        f1=open(f"{parkings[i]}src.txt","w", encoding='utf8')
        f1.write(response.text)
        f1.write('\n')
        f1.close()
    
        tree = etree.parse(f"{parkings[i]}src.txt")
        f2=open(parkings[i]+"trie.txt","a", encoding='utf8')
        today = datetime.datetime.now()
        # print("date local :",today )
        f2.write(f"date local : {today}")
        f2.write('\n')
        for user in tree.xpath("DateTime"):
            # print('Date et heure de la mesure :',user.text)
            f2.write('Date et heure de la mesure :'+user.text+'\n')
        for user in tree.xpath("Name"):
            # print('Nom du parking :',user.text)
            f2.write('Nom du parking :'+user.text+'\n')
        for user in tree.xpath("Total"):
            # print('Nombre total de places :',user.text)
            f2.write('Nombre total de places :'+user.text+'\n')
        for user in tree.xpath("Free"):
            # print('Nombre de places libres :',user.text)
            f2.write('Nombre de places libres :'+user.text+'\n')
        for user in tree.xpath("Status"):
            # print('Statut :',user.text)
            f2.write('Statut :'+user.text+'\n')
        f2.close()

def donneesveloexemple():
    """Recupere les données des velos json et les enregistre dans un fichier"""
    response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_Velomagg.json")
    # print(response.text)
    f1=open("velo.txt","w", encoding='utf8')
    f1.write(response.text)
    f1.write('\n')
    f1.close()




def donneesveloinfo():
    """Recupere les données des velos json et les enregistre dans un fichier"""
    response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json")
    # print(response.text)
    f1=open("informations.txt","w", encoding='utf8')
    f1.write(response.text)
    f1.write('\n')
    f1.close()

def donneesvelodonnees():
    """Recupere les données des velos json et les enregistre dans un fichier"""
    response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
    # print(response.text)
    f1=open("donnes.txt","w", encoding='utf8')
    f1.write(response.text)
    f1.write('\n')
    f1.close()


def parsejsonexemple(): 
    """recupere les donnes json """
    with open('velo.txt') as f:
        data = json.load(f)
        # faire une boucle pour recuperer les noms de toutes les stations de velo 
        name=data["features"][0]["properties"]["nom"]
        # print(name)
        nom=[]
        for i in range(0, len(data["features"])): 
            nom.append(data["features"][i]["properties"]["nom"])
        # print(nom)
        
        # trier les données en fonction de ce qui est recherché 
        
        for i in range(len(nom)):
            f1=open(f"velo_{nom[i]}.txt","a",encoding="utf-8")
            f1.write(f"{nom[i]}"+ "\n" )
            f1.write(f"{data['features'][i]['properties']['installati']}" + "\n")
            f1.write(f"{data['features'][i]['properties']['commune']}" + "\n")
            f1.close()

def parsejsoninfo():
    """lis les donnees et trie les information de informations.txt"""
    with open('informations.txt') as j :
        f2=open("infotrie.txt","w",encoding="utf-8")
        data = json.load(j)
        global nometid
        nometid={}
        for i in range(0, len(data["data"]["stations"])): 
            nometid=f"{data['data']['stations'][i]['name']} : " + f"{data['data']['stations'][i]['station_id']}" + "\n"+ "capacity :" + f"{data['data']['stations'][i]['capacity']}" + "\n" 

            f2.write (f"{data['data']['stations'][i]['name']} : " + f"{data['data']['stations'][i]['station_id']}" + "\n"+ "capacity : " + f"{data['data']['stations'][i]['capacity']}" + "\n" )
            f2.write ("\n")
            # print(nometid)    
        f2.close()

def parsejsonvelo(): 
    """trie les données en fonctions des idées"""
    with open("donnes.txt") as i : 
        f3=open("velotrie.txt", "a", encoding="utf-8")
        data = json.load(i)
        for i in range(0, len(data["data"]["stations"])): 
            f3.write(f"{data['data']['stations'][i]}"+ "\n")
            f3.write("\n")
        f3.close()


def with_delay(park):
    for i in range(336):
        print(f"temps restant : {336-i} secondes")
        donneesparkings(park)
        donneesveloinfo()
        donneesvelodonnees()
        parsejsoninfo()
        parsejsonvelo()
        i=i+1
        sleep(300)