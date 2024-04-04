#!/bin/sh
if [ $# -ne 2 ]
then
    echo "Fournir un paramètre +r, -r, +w ou -w et une extension fichiers"
    exit 1
fi
for fichier in *
do
    if [ -f $fichier ]
    then
        if [ ${fichier##*.} = $2 ]
        then
            echo $fichier
            chmod $1 $fichier
        fi
    fi
done