#module lib
# Copyright © Helec Bastien 
#Version 0.0.1
#2023-01-09

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
        moyenne=somme/len(L)
    print(moyennes)
    
moyenne(L1)
moyenne(L2)

def ecart_type(L):
    """ Calcule l'écart-type des valeurs d'une liste """
    moyenne(L)
    somme = 0
    moyennes
    for i in range(len(L)):
        somme = somme + (L[i]-moyenne)**2
    ecart_type = (somme/(len(L)-1))**0.5
    print(ecart_type)


