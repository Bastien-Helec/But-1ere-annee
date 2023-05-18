#↓ fonction permettant d'afficher un choix entre la conversion farenheit ou celsius
def choix():

    #↓ affiche une demande si on veut une conversion farenheit ou celsius
    print("conversion farenheit ou Celsius :", end=' ')

    #↓ variable de choix entre les 2
    ch=input("")

    #↓ Si ch correspond a farenheit ou f alors faire les informations qui suit
    if ch=="farenheit" or ch=="f" :

        #↓ affectation variable F permettant de recuperer la valeur en farenheit
        F=float(input("valeur en farenheit "))

        #↓ fonction permettant de faire la conversion Farenheit vers Celsius
        def FtoC() :

            #↓ variable C correspondant au calcul en celsius 
            C=(F-32)*(5/9)

            #↓ affiche valeur de F en farenheit equivaut a valeur de C en °C
            print(f"{F} en Farenheit equivaut a {C} °C")

            #↓ Renvoi au debut de la fonction choix
            return choix()

        #↓ Appel de la fonction FtoC dans le if 
        FtoC()
    
    #↓ sinon si la variable ch correspont a Celsuis ou c alors faire les informations qui suit
    elif ch=="Celsius" or ch=="c" :

        #↓ Assignation de la valeur C correspondant a la valeur en celsius
        C=float(input("valeur en celsius "))

        #↓ fonction faisant la conversion de Celsius a Farenheit
        def CtoF():

            #↓ variable F est le calcul en farenheit 
            F=C*(9/5)+32

            #↓ affiche valeur de C en Celsius equivaut a valeur de F en °F
            print(f"{C} en Celsius equivaut a {F}°F")

            #↓ Renvoi au debut de la fonction choix
            return choix()

        #↓ Appel de la fonction CtoF dans le elif
        CtoF()

    #↓ sinon si ch correspond a exit ou leave alors : 
    elif ch=="exit" or ch=="leave" :

        #↓ Affiche fin du programme  
        print("fin du programme")

        #↓ renvoi a une fin de boucle 
        return


    #↓ Sinon 
    else :

        #↓ Afficher rentrer f ou c ; farenheit ou Celsius  
        print("rentrer f ou c ; farenheit ou Celsius")

        #↓ Renvoi au debut de la fonction choix
        return choix()

#↓ appel de la fonction choix  
choix()


