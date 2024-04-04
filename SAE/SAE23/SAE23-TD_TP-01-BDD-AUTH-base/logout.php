<?php
require_once('funcs.php');
###########################################################
# Ici, on déconnecte l'utilisateur
###########################################################
$logout=cbGetValue($_REQUEST,'logout');
if ($logout=='true') {
  session_destroy();
  $_SESSION=array();
  $home='http://'.$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF'];
  header('Location: '.$home);
  // var_dump($_SESSION);
  exit(1);
}
?>
