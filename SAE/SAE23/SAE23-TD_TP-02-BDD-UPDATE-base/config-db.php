<?php
//$pdo=new PDO('mysql:host=localhost;dbname=XXXXXXXXXXXX;charset=UTF8','user','passwd');
$pdo=new PDO('sqlite:auth.sqlite');
$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_ASSOC);
$pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
?>
