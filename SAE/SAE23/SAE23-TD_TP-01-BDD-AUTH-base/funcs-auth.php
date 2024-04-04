<?php
###############################################################################
###############################################################################
function auth($user,$pass) {
  global $pdo;
  if ($user==='toto'&&$pass==='titi') {
    cbPrintf('<h2>Utilisateur [%s] authentifié !</h2>',$user);
    return true;
  }
  if ($user!='') {
    cbPrintf('<h2 style="color:red;">BAD PASSWORD for [%s] !!!</h2>',$user);
  }
  return false;
}
?>
