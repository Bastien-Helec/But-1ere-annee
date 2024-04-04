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