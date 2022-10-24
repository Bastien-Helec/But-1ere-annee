#!/bin/bash 
if [ $# -ne 1 ]; then echo "Fournir un nom en parametre" 
exit 1
fi
    echo "Script : "$0" nom de repertoire: "$1" "  
    mkdir "$1" 
fi
