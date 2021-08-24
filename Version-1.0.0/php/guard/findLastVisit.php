<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "";
$placa = $_GET['placa'];
$query = "SELECT * FROM registro_visitantes WHERE placa = '".$placa."' AND fecha_salida IS NULL AND hora_salida IS NULL";
$response = $connection->query_select($query);
echo json_encode($response);
