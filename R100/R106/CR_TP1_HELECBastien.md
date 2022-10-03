### Helec Bastien - TP1 
---
## Identification et analyse des composants d'un ordinateur :

### Partie A :
### La premiere partie votre objectif sera d'examiner le contenu d'un ordinateur et d'un serveur, mis a disposition par votre enseignant et d'en identifier les composants. 

#### 1. L'unité centrale (UC) :
Quels peripheriques de stockages sont present dans le boitier? 
- 1 disque dur magnetiques (Un stockage non amovible, stockage de travail)
- 1 lecteur de DVD (stockage amovible, stockage de sauvegarde)
- Ils sont connecté sur des bus de données

#### 2. La carte mere :
Combien de slot de barettes de RAM sont présents ? donnez les caractéristiques des barettes présentes . 
-Il y a 4 slots de barettes de RAM DDR4

Combien de connecteurs PCI sont présents ? Combien de connecteurs PCI Express sont présents ? De quels types ?

- 2 connecteurs PCI 
- 1 connecteur PCI express 16x
  
Pouvez vous identifier la position des caches ?
- Non car il sont sous le ventirad proche du Microprocesseur

#### 3. Le serveur :
Quels es la/les differences majeurs avec l'architecture de l'ordinateur ?
- Le serveur ne possede pas d'affichage graphique , il offre une performance superieur mais possede une moins bonne securité qui doit etre compenser 

### Partie B: Utilisation de linux pour l'identification et l'analyse des composants d'un ordinateur : 

#### 4. Information du cpu : 
Indiquez ce que contient le fichier suivant : /proc/cpuinfo

- Processor : Correspond au nombre de processeur 
- Model name : Correspond au nom du processeur
- CPU MHz : Correspond a la frequence du processeur
- Cache size : Correspond a la taille du cache du processeur
- Flags : Correspond aux fonctionnalités du processeur
- apicid : Correspond a l'identifiant du processeur , il correspond a la partie visualisation de l'architecture et des composants du PDF 3 

```
cat /proc/cpuinfo | grep "model name" | grep "cpu MHz" | grep "cpu cores"
```
``` 
cat /proc/cpuinfo | grep "cache size"
``` 
la valeur de cache size est :
8192 KB

Pour savoir si le processeur supporte l'instruction SSE2, utilisez la commande suivante : 
```
cat /proc/cpuinfo | grep "flags"
```
Le processeur supporte l'instruction SSE2

#### 5. information concernant la memoire :
Indiquez ce que contient le fichier suivant : /proc/meminfo

le fichiers suivants permet de voir les informations concernant la memoire

Pour connaitre les informations specifiques a la RAM il faut utiliser la commande suivante : 
```
sudo dmidecode -t 17
```
le -t correspond au type avec le nom 17 
le type de RAM est DDR3 
ça taille est de 8 Go
ça vitesse de 1600 MT/s
et ça tension inconnue 

la commande suivante  :
``` lshw -short -C memory | grep -i empty ``` 
permet de voir les emplacements vides de la RAM
et
``` free -m ```
permet de voir la memoire libre et utilisé

La difference entre lsblk et fdisk -l est que lsblk permet de voir les disques et les partitions, fdisk -l permet de voir les disques et les partitions ainsi que les informations concernant les disques

#### 6. information concernant les bus : 
a l'aide des commandes lspci et lsusb , decrivez et commentez l'architecture physique de la machine sur laquelle vous travaillez.
``` lspci ``` permet de voir les composants connecté sur les bus PCI
ici on peut voir une compatibilité VGA 2 controlleur usb ,3 pci , 1 isa , 1 SATA, 2 ethernet et un controlleur audio 
``` lsusb ``` permet de voir les composants connecté sur les bus USB et non connecté 
ici on peut voir une souris , un clavier , 4 port usb  et un ecran. 

