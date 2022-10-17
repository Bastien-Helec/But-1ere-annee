#### Helec Bastien

### TP3: Programmation shell : 
---

Exercice 1 – Exemple de programme shell 
 
1) Que fait le programme shell suivant, dont le nom est mystere ? 

``` 
#!/bin/sh if [ $# -ne 1 ]; then echo "Fournir un nom en parametre" 
exit 1
fi
if  ( test -d "$1" ); then
    echo "Répertoire "$1" existe déja" exit 0
else 
    echo "Script : "$0" nom de repertoire: "$1" "  
    mkdir "$1" 
fi
```

Ce programme shell permet de créer un répertoire dont le nom est en argument. 
Si le répertoire existe déjà, le programme affiche un message d'erreur.

2) Proposez un exemple d'appel du programme mystere.

```
mystere.sh test
```

Exercice 2 – La boucle while 
 
Écrire un programme shell qui affiche les arguments du programme, dans  l'ordre d'apparition 
(1er argument en premier). Si le programme n'a aucun argument, afficher « sans argument ». 
 
Indication  : Utilisez la commande shift ainsi que les arguments ($x).

```
#!/bin/sh
while [ $# -gt 0 ]
do
    echo $1
    shift
done
```

Ce programme permet d'afficher les arguments du programme dans l'ordre d'apparition.

Exercice 3 – La boucle for 
 
Écrire  un  programme  shell  qui  affiche  tous  les  sous-répertoires  du  répertoire  courant,  en 
utilisant une boucle.   <br>

Indication  : Utilisez une variable (ex : rep) et le symbole joker *. Testez pour chaque 
occurrence le type (-d pour directory). 

```
#!/bin/sh
for rep in *
do
    if [ -d $rep ]
    then
        echo $rep
    fi
done
```

Ce programme permet d'afficher tous les sous-répertoires du répertoire courant.

Exercice 4: 

1) Écrire un programme shell qui accepte 2 paramètres. Le premier paramètre est +r, -r, +w ou 
-w, et le deuxième paramètre spécifie une extension de nom de fichiers. En fonction de la valeur du  premier  paramètre,  le  programme  modifiera  les  droits   du  groupe  de  tous  les  fichiers  du répertoire courant dont l'extension est égale au deuxième paramètre.

Pour  contrôle,  avant chaque 
modification des droits sur un fichier, le programme affichera le nom du fichier. 
 
Exemple d'utilisation (le script s'appelle droitsfichiers) : 

droitsfichiers +w .txt

```
#!/bin/sh
if [ $# -ne 3 ]
then
    echo "Fournir un paramètre +r, -r, +w ou -w et une extension fichiers"
    exit 1
fi
for fichier in *
do
    if [ -f $fichier ]
    then
        if [ ${fichier##*.} = $3 ]
        then
            echo $fichier
            chmod $1 $fichier
            
        fi
    fi
done
```

