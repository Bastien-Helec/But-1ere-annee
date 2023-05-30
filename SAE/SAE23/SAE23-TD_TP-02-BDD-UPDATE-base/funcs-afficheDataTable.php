<?php
function afficheTH($val) {
  printf("<th>%s</th>\n",$val);
}
function afficheTD($val) {
  printf("<td>%s</td>\n",$val);
}
function afficheTRTD($val,$attr='') {
  if ($attr!='') printf("<tr><td %s>%s</td></tr>\n",$attr,$val);
  else printf("<tr><td>%s</td></tr>\n",$val);
}
function afficheTRTHTD($key,$val) {
  printf("<tr><th>%s</th><td>%s</td></tr>\n",$key,$val);
}
function afficheDataTable($data) {
  if (is_array($data)) {
    printf("<table>\n");
    printf("<tr>"); 
    foreach (array_keys(current($data)) as $i=>$colName) {
      printf("<th>%s</th>",$colName);
    }
    printf("</tr>\n");
    foreach ($data as $i=>$row) {
      printf("<tr>"); 
      foreach ($row as $key=>$val) {
        printf("<td>%s</td>",$val);
      }
      printf("</tr>\n");
    }
    printf("</table>\n");
  } else {
    printf("<h2 style='color:red;'>Erreur de données !!!</h2>\n");
  }
}
?>
