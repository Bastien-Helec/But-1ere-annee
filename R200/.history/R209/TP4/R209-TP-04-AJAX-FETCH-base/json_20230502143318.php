<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');
$r=@file_get_contents('https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220.json');
echo ($r)?$r:'{"error":"NOT FOUND !"}';
exit(0);
?>
