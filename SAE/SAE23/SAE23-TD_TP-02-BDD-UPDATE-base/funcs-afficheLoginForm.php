<?php
###############################################################################
###############################################################################
function afficheLoginForm() {
  global $pdo;
  cbPrintf('<fieldset class="loginForm">');
  cbPrintf('<legend>Authentification</legend>');
  cbPrintf('<form action="%s" method="post" accept-charset="utf8">',$_SERVER['PHP_SELF']);
  cbPrintf('<table class="loginForm">');
  cbPrintf('<tr class="loginForm">');
  cbPrintf('<th class="loginForm">Utilisateur :</th>');
  $user=cbGetValue($_REQUEST,'user');
  cbPrintf('<td class="loginForm">');
  cbPrintf('<input type="text" name="user" value="%s"/>',$user);
  cbPrintf('</td>');
  cbPrintf('</tr>');
  cbPrintf('<tr class="loginForm">');
  cbPrintf('<th class="loginForm">Mot de passe :</th>');
  cbPrintf('<td class="loginForm">');
  cbPrintf('<input type="password" name="pass"/>');
  cbPrintf('</td>');
  cbPrintf('</tr>');
  cbPrintf('<tr class="loginForm">');
  cbPrintf('<th class="loginFormCenter" colspan="2">');
  cbPrintf('<input type="submit" value="Authentification"/>');
  cbPrintf('</th>');
  cbPrintf('</tr>');
  cbPrintf('</table>');
  cbPrintf('</form>');
  cbPrintf('</fieldset>');
  include('html-fin.php');
}
?>
