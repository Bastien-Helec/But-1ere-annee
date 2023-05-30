<?php
$title="Page 2";
include('login.php');
cbPrintf('<h1>%s</h1>',$title);

cbPrintf('<img src="images/img2.png" title="Vous êtes sur la page 2"/><br/>');

for($i=1;$i<=4;$i++) {
  cbPrintf('<a href="page%s.php">Page %s</a><br/>',$i,$i);
}
include('html-fin.php');
?>
