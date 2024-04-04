<?php
require_once('funcs-afficheDataTable.php');
function usersCheckExists($user,$id) {
  global $pdo;
  return true;// OK si 0 utilisateurs trouvés
}
function usersUpdateByID($id) {
  global $pdo;
  if (intval($id)>0) {
    cbPrintf('<h2 class="ok">Modification de l\'utilisateur #%s effectuée</h2>',$id);
  } else {
    cbPrintf('<h2 class="err">Modification de l\'utilisateur #%s impossible !!!</h2>',$id);
  }
  usersList();
}
?>
