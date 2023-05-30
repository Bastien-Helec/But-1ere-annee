<?php
require_once('funcs.php');
require_once('config-db.php');
cbPrintf('<!DOCTYPE html>');
cbPrintf('<html');
cbPrintf('<head>');
if (isset($title)) {
  cbPrintf('<title >%s</title>',$title);
}
cbPrintf('<meta charset="utf8"/>');
cbPrintf('<link rel="stylesheet" href="login.css"/>');
cbPrintf('</head>');
cbPrintf('<body>');
?>
