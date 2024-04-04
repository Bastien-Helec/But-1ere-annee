import random as rand

import numpy as np #importation de numpy
import matplotlib.pyplot as plt



# Bx1= [i+rand.randint(-6,7)/10 for i in X1]

# q=0.5 # pas de quantification 

# X1q = q*np.round(X1/q) # signal quantifié 

# E=X1-X1q #ereur de quantification 


#3)

# F2=2 #assigniation d'un variable F a valeur 2

# T2=np.linspace(0.2,1,1001) #Assigniation de la variable T avec le module numpy pour creer un espace de ligne compris entre 0 et 1001 avec un pas de 1

# X2=np.sin(F2*np.pi*2*T2)#Assigniation de la varibale X1 avec le module numpy pour creer une sinusoide avec la varibale F la valeurs pi du module numpy et la variable T 

#4) 
# X3=X1+X2 #Addition des deux courbes X1 et X2
#2)3) 

# plt.plot(X1 , marker='o', color='tab:purple', label='X1') #Affichage de la courbe X1
# plt.plot(Bx1, color='tab:purple', label='Bruit de X1')
# plt.plot(X1q, color='tab:red', label='Signal quantifié')
# plt.plot(E, color='tab:cyan', label='Erreur de quantification')
# plt.plot(Xech, marker='o', color='tab:blue', label='signal echantilloné')

# plt.plot(X2, marker='o', color='r', label='X2') #Afffichage de la courbe X2
# plt.plot(X3, marker='o', color='y', label='X3') #Afffichage de la courbe X3
# plt.plot(F)# Y=2 car valeurs de F=2

# 12)
F=2 #assigniation d'un variable F a valeur 2
T=np.linspace(0,1,1001) #Assigniation de la variable T avec le module numpy pour creer un espace de ligne compris entre 0 et 1001 avec un pas de 1  
X1=np.sin(F*np.pi*2*T) #Assigniation de la varibale X1 avec le module numpy pour creer une sinusoide avec la varibale F la valeurs pi du module numpy et la variable T 

Te=0.02 #assigniation d'un variable Te a valeur 0.02 (20ms)
Te2=np.arange(0,1,Te) #Assigniation de la variable Te2 avec le module numpy pour creer un espace de ligne compris entre 0 et 1 avec un pas de 0.02 (20ms)

Xech=np.sin(F*np.pi*2*Te2) #Assigniation de la varibale Xech avec le module numpy pour creer une sinusoide avec la varibale F la valeurs pi du module numpy et la variable Te2

plt.plot(T, X1, label='X1 (continu)') #Affichage de la courbe X1
plt.plot(Te2, Xech, marker='o' ,label='Xech (échantillonné)') #Affichage de la courbe Xech

# 13)



plt.xlabel("Secondes") #Axes x =Secondes
plt.ylabel('Amplitude')#Axes y= Amplitude
plt.title("Echantillonage en fonction de l'amplitude") #Titre du graphe
plt.legend() #Affiche la legendE
plt.grid(True) #affichage de la grille
plt.show() #Afficher le plot
plt.close() #Fermer le plot


