from lib import with_delay

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

# pour chaque parking voiture on recupere les donnees de fichiers trie on stocke dans une liste la date et heure de la mesure , le statut et on stocke dans une liste le nombre de place occupé en faisant le calcul du nombre de place total - nombre de place libre
plbr=[]
stat=[]
# for i in range(22):
#     f6=open("FR_MTP_ARCEtrie.txt","r", encoding='utf8')
#     lines=f6.readlines()
#     f6.close()
#pour chaque ligne dans la liste de chaque ligne de parking
    

    # for l in range(5,len(lines), 6) :
    #     stat.append(lines[l])
    # stats=stat[0]
    # stats=stats.split(':')

    # if stats[1]=='Open\n':
    #     # print("open")
    #     statu=1

    # else:
    #     statu=0
    #     print("close")

    ### Où se trouve l'erreur ? 
    # liste les places libres mais problemes a ce niveau de boucle (renvoi la premiere valeur uniquement du fichier texte)
    ### Problème résolu ?
    # for d in range(4,len(lines),6):
    #     for j in range(0, len(lines)), 6:
    #         plbr.append("".join([lines[d], lines[d+1], lines[d+2], lines[d+3], lines[d+4], lines[d+5]]))
    #         plbre=plbr[0]
    #         plbre=plbre.split(':')
    #         print(plbre)

def ExtractData(listParking : list[str]):
    data = []
    
    for park in (parkings):
        with open(park + "trie.txt", 'r', encoding = "utf-8") as file:
            data.append(file.readlines())
    return data
AllData = ExtractData(parkings)
print(AllData[0])

def CleanData(data : list[list[str]]):
    for place in parkings:
        for elem in place:  
            elem.replace('\n', '')
    return data

def ExtractDataFromAPark(data : list[str]):
    newData = []
    oldInd = 0
    for ind in range(0, len(data), 6):
        place = data[oldInd:ind] # Slice
        if place[5].split(':') == "Open":
            localDate, actualDate, name, numberAllPlace, freePlace, statut = place
            newData.append([localDate, actualDate, name, numberAllPlace, freePlace])
        oldInd = ind
    return newData

def ExtractOpenStatut(data : list[list[str]]):
    newData = []
    for place in data:
        newData.append(ExtractDataFromAPark(place))
    return newData

print(ExtractOpenStatut(CleanData(ExtractData(parkings))))

# for place in parkings:
#     for e in place:
#         e.replace('\n', '')