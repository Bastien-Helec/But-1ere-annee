<?php
require_once('funcs-afficheDataTable.php');
function usersList() {
  global $pdo;
  $stmt=$pdo->prepare('SELECT * FROM "users" ORDER BY "user"');
  if ($stmt->execute()) {
    printf("<table>\n");
    $entete=false;
    while ($row=$stmt->fetch()) {
      if(!$entete) {// Affiche l'entete 1 seule fois
        $entete=true;
        printf("<tr>");
        afficheTH('id');
        afficheTH('user');
        afficheTH('pass');
        afficheTH('mail');
        printf("</tr>\n");
      }
      printf("<tr>");
      $id=cbGetValue($row,'id');
      $user=cbGetValue($row,'user');
      $pass=cbGetValue($row,'pass');
      $mail=cbGetValue($row,'mail');
      afficheTD($id);
      afficheTD($user);
      afficheTD($pass);
      afficheTD($mail);
      printf("</tr>\n");
    }
    printf("</table>\n");
    $stmt->closeCursor();
  }
}
?>
