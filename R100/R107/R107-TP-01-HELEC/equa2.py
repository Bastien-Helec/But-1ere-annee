#2.3 

    #↓ assignation des valeurs pour l'equations
a,b,c= 2,2,2
    
#↓ calcul de delta
d=b**2-4*a*c

#↓ affichage de l'équation
print(f'Equation: {a}x²+{b}x+{c}')

#↓ affichage de delta 
print(f'Delta: {d}')

#↓ fonction permettant de calculer les racines
def racine():

#↓ si delta est superieur a 0
    if d>0:
        #↓ racine de x1 qui est -b-racine de d/2a\
        x1=(-b-sqrt(d))/(2*a)

        #↓ racine de x1 qui est -b-racine de d/2a
        x2=(-b+sqrt(d))/(2*a)

        #↓ affichage des 2 racines
        print(x1,x2)
        #↓ sinon si d=0 racine double
    elif d==0 :
        #↓ calcul pas besoin de sqrt racine double
        x1=-b/(2*a)
    
        #↓ affichage de la racine double
        print(x1)
    
    #sinon
    else :
        #↓ affichage pas de solution pour l'équation actuel
        print("pas de solution pour l'équation actuel")

    #↓ appel de la fonction racine\n",
    racine()