<?php
###############################################################################
###############################################################################
function auth($user,$pass) {
  global $pdo;
  $stmt=$pdo->prepare('SELECT * FROM "users" WHERE "user"=:u AND "pass"=:p');
  $stmt->execute(array('u'=>$user,'p'=>$pass));
  $rows=$stmt->fetchAll();
  $stmt->closeCursor();
  //var_dump($rows);
  if (count($rows)===1) {
    cbPrintf('<h2>Utilisateur [%s] authentifié !</h2>',$user);
    return true;
  }
  if ($user!='') {
    cbPrintf('<h2 style="color:red;">BAD PASSWORD for [%s] !!!</h2>',$user);
  }
  return false;
}
?>
