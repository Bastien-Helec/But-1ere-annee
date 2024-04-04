#### Helec Bastien

#### TP4 : Programmation shell - suite
 
---

Exercice 1 – Utilisation des variables d’environnement 

Ecrire un script qui affiche « Vous êtes l’utilisateur x sur la machine y, votre répertoire 
utilisateur est z » en utilisant les variables d’environnement.

X étant le nom d’utilisateur, Y le nom de votre machine et z votre répertoire personnel.

``` 
#!/bin/bash
echo "Vous êtes l'utilisateur $USER sur la machine $HOSTNAME, votre répertoire utilisateur est $HOME"
```

Exercice 2 – Statut d’exécution 
 
1. Faire un script qui utilisera la commande mkdir et qui permettra de créer un 
répertoire. Votre script recevra le nom du répertoire à créer en tant 
qu'argument. 

```

#!/bin/bash 
if [ $# -ne 1 ]; then echo "Fournir un nom en parametre" 
exit 1
fi
    echo "Script : "$0" nom de repertoire: "$1" "  
    mkdir "$1" 
fi
```

 
Il existe une variable spéciale qui contient après l'exécution de chaque commande le  statut 
d'exécution de celle-ci sous la forme d'un nombre (=0 si l’exécution s’est bien déroulée). 
 
2. Rechercher sur Internet le nom de cette variable et modifier votre script 
précédent pour faire afficher ce statut. 

```
#!/bin/bash 
if [ $# -ne 1 ]; then echo "Fournir un nom en parametre" 
exit 1
fi
    echo "Script : "$0" nom de repertoire: "$1" "  
    mkdir "$1"
    echo "Statut : $?" 
fi
```

Utiliser votre script pour créer un répertoire dans un dossier où vous détenez les 
droits suffisants (home). 
    
    ```
    ./script.sh test
    ``` 
Utiliser ce script pour créer un répertoire dans un dossier où vous ne disposez pas 
des droits suffisants (/root). 

``` 
./script.sh test
```

Comparer les résultats des statuts obtenus lors des deux questions précédentes et en 
déduire l'utilité de cette variable spéciale

Dans le repertoire ou on detiens les droits suffisant la commande renvoi un 0 , dans le repertoire ou l'on ne detiens pas les droits suffisant la commande renvoi un 1.

Ce qui veut dire que la commande s'est bien déroulée dans le premier cas et pas dans le second.

Exercice 3 – Petit jeu 
 
Écrire un programme shell qui permet de faire saisir à une personne un nombre compris entre 
1 et 100 et d’effacer la saisie ensuite. Cette valeur sera stockée dans une variable. Vous devrez ensuite 
par comparaison à la variable saisir une chiffre et afficher « plus grand »  si la variable de départ est 
plus grande, « plus petit » si la variable de départ est plus petite et « Bravo tu as trouvé ! » si vous 
avez saisi la bonne valeur.
Indication  : Utilisez des variables, la commande read, la commande clear

```
#!/bin/bash
echo "Saisir un nombre entre 1 et 100"
read nombre
clear
if [ $nombre -gt 100 ]; then
    echo "Plus petit"
elif [ $nombre -lt 1 ]; then
    echo "Plus grand"
else
    echo "Bravo tu as trouvé !"
fi
```