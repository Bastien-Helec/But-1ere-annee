<?php
$title="Page 3";
include('login.php');
cbPrintf('<h1>%s</h1>',$title);

cbPrintf('<img src="images/img3.png" title="Vous êtes sur la page 3"/><br/>');

for($i=1;$i<=4;$i++) {
  cbPrintf('<a href="page%s.php">Page %s</a><br/>',$i,$i);
}
cbPrintf('<a href="index.php">Sommaire</a><br/>');
include('html-fin.php');
?>
