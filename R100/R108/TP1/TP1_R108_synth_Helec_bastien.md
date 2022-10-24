#### Helec Bastien              
### TP1: Systeme de fichiers : 
--- 

1. Repertoire utilisateur : 
    1. Affichez la valeur du repertoire utilisateur.
    ```
    echo $HOME
    ```
    2. Affichez la valeur du répertoire courant.
    ```
    pwd
    ```
    
    1. Quel est donc le répertoire courant après ouverture d’une session ?
    ``` 
    /home/utilisateur
    ``` 
    
    1. Déplacez-vous vers la racine en une commande
    ```
    cd $HOME
    ```

    1. Faites afficher sous forme de liste les fichiers et dossiers présents en recherchant dans la
    documentation de ls
    
    ``` 
    ls -C -a -1
    ``` 

2. Editeurs de texte:
    Pour éditer un fichier texte, il suffit de lancer l’application nano en précisant en argument le chemin
vers le fichier (Exemple : nano toto). Si le fichier existe, il est ouvert, sinon il est créé et ouvert. 
</br>

   1. Retournez dans votre dossier personnel en une seule commande :
    ```
    cd $HOME
    ``` 
    2. Tapez un mot dans le fichier puis sauvegarder les données.
    ``` 
    nano toto
    ```

    Ctrl+x pour quitter et ctrl+s pour sauvegarder

    3. Vérifiez que la taille du fichier et comparez-la au nombre de caractères tapés.
    ```
    ls -l 
    ``` 
    dans nano quand rien n'est ecrit la valeur est a 0 

    j'ai alors ecris :
    ``` 
    coucou toto
    ``` 
    4. Concluez ?
    la valeur est ensuite passez a 12 soit un octet de plus que le texte
    <br>
    La commande cat permet d’afficher, dans la console, le contenu d’un fichier texte
    5. Faites afficher le contenu de votre fichier.
    ```
    cat toto
    ```

3. Creation d'une arborescence donnée: 
    
    1. Déplacez-vous dans votre répertoire utilisateur.
    ```
    cd $HOME
    ```
    
    2. Affichez le contenu du répertoire utilisateur.
    ```
    pwd
    ```
    
    3. Effacez en un minimum de commandes, tous les fichiers et répertoires existant dans le
    répertoire utilisateur (sauf votre compte-rendu !).
    ```
    shopt -s extglob
    rm !(TP1_R108_Synth_Bastien_Helec| TP1_R108_log_Bastien_Helec)
    ``` 
    
    4. Vérifiez le résultat.</br>
    cela a bien supprimer tout sauf le compte_rendu et le fichier log 
    </br>
    2. Créez l'arborescence suivante en utilisant des noms absolus et sans changer de répertoire
    courant. Attention, / et /tmp existent déjà
    ``` 
    sudo mkdir ./tmp/rt1 | mkdir ./tmp/rt1/xyz 
    sudo mkdir ./tmp/rt1/xyz/public_html ./tmp/rt1/xyz/programmes
    sudo mkdir ./tmp/rt1/xyz/public_html/docs ./tmp/rt1/xyz/public_html/images
    sudo touch ./tmp/rt1/xyz/public_html/index.html 
    sudo mkdir ./tmp/rt1/xyz/programmes/java ./tmp/rt1/xyz/programmes/langage_c ./tmp/rt1/xyz/programmes/php
    sudo touch ./tmp/rt1/xyz/programmes/java/TP.java
    sudo touch ./tmp/rt1/xyz/programmes/langage_c/a.c
    ```
    1. Modifiez le contenu de index.htm pour écrire le texte : <h1>Bonjour !!!</h1>.
    
    ```
    echo <h1>Bonjour</h1> > /tmp/rt1/xyz/public_html/index.htm 
    ```
    2. Vérifiez le contenu du ficher avec une commande.
    </br>
    ```
    cat /tmp/rt1/xyz/public_html/index.htm 
    ``` 
    3. Copiez le contenu du répertoire programmes dans le répertoire images.
    ```
    cp /tmp/rt1/xyz/programmes /tmp/rt1/xyz/public_htm/images  
    ```
    4. Déplacez toute la partie programmes dans le répertoire docs.

    ```
    mv /tmp/rt1/xyz/programmes /tmp/rt1/xyz/public_htm/docs
    ```

    5.   Affichez le contenu détaillé du répertoire docs.
    ```
    ls -l
    ```