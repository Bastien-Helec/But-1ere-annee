<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');
$r=@file_get_contents('https://data.montpellier3m.fr/');
echo ($r)?$r:'{"error":"NOT FOUND !"}';
exit(0);
?>
