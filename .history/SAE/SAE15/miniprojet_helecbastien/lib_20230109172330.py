#module lib
# Copyright © Helec Bastien 

# Instant de la mesure (H)
T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Série 1 : températures ( °C )
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]

# Série 2 : températures ( °C )
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]

def moyenne(L):
    """ Calcule la moyenne des valeurs de la liste L """
    somme = 0
    for i in range(len(L)):
        somme = somme + L[i]
    return somme / len(L)
    


