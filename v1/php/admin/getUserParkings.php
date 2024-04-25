<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$id_usuario = $_GET["id_usuario"];
$query = "SELECT parqueadero.id, parqueadero.codigo FROM usuario_parqueadero t_rompimiento 
INNER JOIN parqueadero ON t_rompimiento.id_parqueadero = parqueadero.id WHERE t_rompimiento.id_usuario = ".$id_usuario;
$response = $connection->query_select($query);
echo json_encode($response);