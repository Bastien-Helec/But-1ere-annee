<?php
require_once('funcs-afficheDataTable.php');
function usersUpdateFormByID($id) {
  global $pdo;
  cbPrintf('<h2>Utilisateur #%s</h2>',$id);
  cbPrintf('<form action="%s" method="post" accept-charset="utf8">',$_SERVER['PHP_SELF']);
  cbPrintf('<table class="update">');
  $input=sprintf('<input type="text" name="id" value="%s"/>',$id);
  afficheTRTHTD('Numéro :',$input);
  afficheTRTD('<input type="submit" value="Mise à jour"/>','colspan="2"');
  cbPrintf('</table>');
  cbPrintf('</form>');
}
?>
