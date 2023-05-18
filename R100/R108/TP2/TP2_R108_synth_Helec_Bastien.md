#### Helec Bastien

### TP1: Commandes UNIX : 
---

Exercice 1 – Créations, suppressions et droits d'accès
1) A l’aide de commandes, créez l’arborescence donnée ci-dessous et déplacez-vous à
l’intérieur.

```
cd ~ 
mkdir cours | mkdir tp |touch README | touch LISEZMOI

cd cours
touch notes 1 | touch notes 2
```

<br>
2) Par défaut, quels sont les droits d'accès des fichiers crées ? Et répertoires créés ?

```
ls -l 
``` 
les repertoires et fichiers ont les droits d'accès : drwxr-xr-x

3) Rajouter le droit d'écriture pour le tous au fichier notes1. 
```
chmod u+w notes1
```

4) Modifier les droits d'accès du fichier LISEZMOI pour qu'ils soient à 521. Vérifiez par une
commande.

```
cd ~
chmod 521 LISEZMOI
```

5) Supprimer ensuite tous les répertoires et fichiers créés.

``` 
rm -r -d cours | rm -r -d tp | rm README | rm LISEZMOI
```

Exercice 2 – Copies et déplacements de fichiers
1) Dans votre home directory, créer un répertoire essai.

```
cd ~ 
mkdir essai
```

2) Copier les fichiers /etc/passwd et /etc/group dans le répertoire essai sous des noms
différents.
```
cp /etc/passwd essai/passwd
```



3) Créer dans essai un répertoire copies.

``` 
cd essai
mkdir copies
```

4) Déplacer un des fichiers de essai dans copies.

```
mv passwd copies/passwd
```


5) Créer un répertoire titi dans copies.

```
mkdir copies/titi
```

6) Supprimer le droit d'exécution 'x' pour le répertoire copies.

```
chmod -x copies
```

7) Taper ls copies. Que remarquez-vous?

```
ls copies
```
On remarque que le dossier copies n'est plus en bleu, il est en noir.

8) Détruire le contenu du répertoire copies avec la commande rm. Que remarquez-vous?

``` 
rm -r copies
```

9)  Ajoutez le droit d'exécution 'x' pour le répertoire copies.

```
chmod +x copies
```

10) Chercher à l’aide de man l’option de la commande rm permettant de détruire le répertoire
copies.
```
man rm
rm -d
```


Exercice 3 – Visualisation de fichiers dans le terminal

1) Afficher le contenu du fichier /usr/include/dialog.h avec la commande cat.

```
cat /usr/include/dialog.h 
```
2) Faire cat sans nom de fichier. Que remarquez-vous? Sortir avec CTR-D.

```
cat
```
On remarque que cat attend une entrée standard, on peut donc écrire dedans.

3) Faire cat /etc/group.
   
``` 
cat /etc/group
```

4) Afficher le même fichier avec la commande more.

```
more /etc/group
```


5) Faire whatis ls. 

```
whatis ls
```
Que remarquez-vous?
whatis ls permet de savoir ce que fait la commande ls.

De même avec whereis et which.
```whereis ls
which ls
```
whereis ls permet de savoir où se trouve la commande ls
et which ls permet de savoir quelle commande ls est utilisée.

Exercice 4 – Liens symboliques
On se propose de tester la commande ln. Pour cela :
1) Créer un fichier de test nommé original et un lien physique sur ce fichier nommé
physique.
Ecrivez à l’aide de nano du texte (une 20e de caractères) dans le fichier original.

```
nano original
ln original physical
```
2) Ouvrir les fichiers original et physique. Que constate-t-on après édition du fichier
physique ?

```
nano original
```
On constate que le fichier original a été modifié.

3) Créer un lien symbolique sur ce fichier nommé symbolique.

```
ln -s original symbolic
```

4) Faites un ls -l. Que constatez-vous ?

```
ls -l
```
On constate que le lien symbolique a tout les droits d'accès en plus du fichier original.

1) Modifier le contenu du fichier original.Que constate-t-on au niveau du fichier
symbolique ? Et au niveau du fichier physique ?

```
nano original
```
On constate que le fichier original a été modifié.
on constate aussi que les fichiers symbolique et physique ont changer en meme temps que original 

6) Effacer le fichier original puis ouvrir le fichier symbolique. Que se passe-t-il ?

```
rm original
cat symbolique
cat physique
ls
```
en faisant ls on peut voir que symbolique a changer de couleurs 

comme symbolique est un lien symbolique cela veut dire que si le fichier parents est supprimer les fichiers enfants non pas de contenu , contrairement a un lien physique ou le fichier enfant a le meme contenu que le fichier parent meme en etant supprimer 

7) Ouvrez le fichier physique. Que se passe-t-il ? Concluez.

``` 
cat physique
```
le fichier physique a toujours le contenu de original meme si original a été supprimer

Exercice 5 – La commande ls

Placez-vous dans votre répertoire d'accueil et précisez les options à utiliser pour la commande ls dans les cas listés ci-dessous. Pour connaître la liste des options, consultez le manuel
en ligne en tapant :
• man ls.

```
cd ~
```

1) Listage simple.

```
ls 
```

2) Listage incluant les fichiers cachés ou ceux qui commencent par ".". On remarquera la
présence des 2 fichiers "." et ".."

```
ls -a 
```


3) Listage avec descriptif complet de chaque référence : droits, nombres de liens, dates,
taille user group, etc.

```
ls -l
```

4) Créez des sous-répertoires ainsi que des fichiers dans ces répertoires et faites un
listage récursif du contenu de tous ces sous-répertoires. Puis un listage récursif détaillé.

```
mkdir test
cd test
mkdir test2
cd test2
nano test
cd ..
cd ..
ls -R
ls -Rl
```
ls -Rl permet de lister les fichiers et les sous dossiers de manière récursive avec les détails de chaque fichier

5) Listage par ordre chronologique, et inverse.

```
ls -t
ls -r
```
ls -t permet de lister les fichiers par ordre chronologique

6) Listage simple du contenu du répertoire, avec spécification du type de fichier :
répertoire /, lien symbolique @, exécutable * .

```
ls -F
```
-F permet d'ajouter un caractère à la fin du nom du fichier pour indiquer son type.

Exercice 6 – La commande grep
Effectuez les recherches suivantes sur ce dictionnaire à l’aide du « filtre » grep sur le fichier dico_francais.txt. (à télécharger depuis Moodle et à déposer dans votre répertoire
personnel) :

1) Liste des mots se terminant par les lettres « cot ».

```
cat dico_francais.txt | grep cot$
```

2) Mots commençant par « ab » et se terminant par « t ».

```
cat dico_francais.txt | grep ^ab.*t$
```


3) Mots commençant par une lettre dans l’intervalle [a-l].

```
cat dico_francais.txt | grep ^[a-l]
```

4) Compter le nombre de mots commençant par « V ».

```
cat dico_francais.txt | grep ^V | wc -l
```
wc permet de compter le nombre de ligne, de mot et de caractère avec l'option -l on compte le nombre de ligne du grep ^V