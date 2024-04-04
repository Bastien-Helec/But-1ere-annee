#2.2

# assignation des valeurs en input taille est masse
t=float(input('entrer votre taille en mètres'))
m=float(input('entrer votre masse en kilo'))

# function IMC permettant de calculer l'IMC
def IMC():

    #calcul de l'IMC
    tcarré=t*t
    imc=m/tcarré

    #si l'IMC est inferieur a 25
    if imc<25 : 

        #afficher vous n'etes pas en surpoids car {imc}<25
        print(f"vous n'etes pas en surpoids car {imc}<25")
    
    #sinon
    else :

        #afficher vous etes en surpoids car {imc}>25
        print(f"vous êtes en surpoids car {imc}>25")
#appel de la fonctin IMC
IMC()

