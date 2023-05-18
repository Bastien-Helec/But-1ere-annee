<?php
printf("<!DOCTYPE html>\n");
printf("<html>\n");
printf("<head>\n");
printf("<title>Football</title>\n");
printf("<meta charset=\"utf-8\"/>\n");
printf("<link rel=\"stylesheet\" href=\"foot.css\"/>\n");
printf("</head>\n");
printf("<body>\n");
printf("<h1>Liste des équipes</h1>\n");
$data=array(
  array('id'=>5,'nom'=>'Montpellier'),
  array('id'=>8,'nom'=>'Paris SG'),
  array('id'=>9,'nom'=>'Monaco'));
foreach ($data as $i=>$row) {
  printf("Equipe(%d) = %s<br/>\n",$row['id'],$row['nom']);
}
printf("</body>\n");
printf("</html>\n");
?>
