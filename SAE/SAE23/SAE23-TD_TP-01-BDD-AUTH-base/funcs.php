<?php
###############################################################################
# Renvoi la valeur de la case $name d'un tableau (ou '' si elle n'existe pas)
###############################################################################
function cbGetValue($array,$name,$default='') {
  if (isset($array[$name])) return $array[$name];
  else return $default;
}
###############################################################################
# Affiche les arguments comme avec un printf(), mais toujours avec \n à la fin
# cbPrintf('X=%d',42); est équivalent à printf("X=%d\n",42);
###############################################################################
function cbPrintf() {
  $args=func_get_args();
  if (count($args)===0) $args=array('');
  $args[0].="\n";
  call_user_func_array('printf',$args);
}
####################################################
## Liste des fonctions à charger
####################################################
require_once('funcs-afficheLoginForm.php');
require_once('funcs-auth.php');
?>
