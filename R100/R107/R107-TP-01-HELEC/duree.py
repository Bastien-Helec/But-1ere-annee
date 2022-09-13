#1.5 TD1

#↓ assignation des valeurs jour heure min seconde a la suite
j,h,m,s=1,3,26,5

#↓ function convertit jour heure min en sec  
def calculensec() :

    #↓ 24h dans 1 jours
    h1=h+(j*24)

    #↓ 60 min dans 1 h
    m1=m+(h*60)

    #↓ 60sec dans 1 min
    s1=s+(m*60)

    #affiche le resultat en secondes  
    print (f'{s1} secondes')

calculensec()

#1.6 TD1

#↓ x est la valeur par defaut qui nous est demande de reconfigurer en horloge    
x=654321

#↓ function permettant le calcul par jours , heures, minutes , secondes
def calculformhorloge() :

    #↓ conversion de sec en jours 

    j=x/(86400)

    #↓ conversion avec suppression de l'entier précedent permattant resepctivement de calculer heure , minutes et secondes
    
    h=(j-int(j))*24
    m=(h-int(h))*60
    s=(m-int(m))*60

    #↓ affichage du resultats
    print(f'{x}sec equivaut a ,{int(j)}j {int(h)}h {int(m)}min {int(s)}sec')

#↓ appel de la function calculformhorloge
calculformhorloge()