<?php
try {
  $pdo=new PDO('mysql:host=localhost;charset=utf8;dbname=base','user','passwd');
  $statement=$pdo->query("SELECT * FROM equipes");
  while($row=$statement->fetch(PDO::FETCH_ASSOC)) {
    printf("Nom de l'équipe : [%s]\n",$row['nom']);
  }
  $statement->closeCursor();
}
catch (Exception $e) {
  printf("ERREUR : %s !!!\n",$e->getMessage());
}
?>
