<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "";
$length = count($_GET);
$keys = array_keys($_GET); // obtiene los nombres de las varibles
$values = array_values($_GET); // obtiene los valores de las varibles
$query = "SELECT id,dinero_final FROM turno ORDER BY id DESC LIMIT 1";
$response = $connection->query_select($query);
echo json_encode($response);
