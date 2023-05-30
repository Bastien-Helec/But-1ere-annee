<?php
$title='Base des utilisateurs';
include('login.php');
require_once('funcs-usersList.php');
require_once('funcs-usersUpdateFormByID.php');
require_once('funcs-usersUpdateByID.php');
cbPrintf('<h1>%s</h1>',$title);

$action=cbGetValue($_REQUEST,'action');
$id=cbGetValue($_REQUEST,'id');
//var_dump($_SESSION);
var_dump($_REQUEST);
switch($action) {
  case 'update':usersUpdateByID($id);break;
  case 'updateForm':usersUpdateFormByID($id);break;
  default:usersList();break;
}
cbPrintf('<table class="menu"><tr class="menu">');
for($i=1;$i<=4;$i++) {
  cbPrintf('<td><a href="page%s.php">Page %s</a></td>',$i,$i);
}
cbPrintf('<td><a href="index.php" title="Sommaire">Sommaire</a></td>');
cbPrintf('</tr></table>');
include('html-fin.php');
?>
