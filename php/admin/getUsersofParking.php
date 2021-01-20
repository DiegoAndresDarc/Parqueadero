<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$id_parqueadero = $_GET["id_parqueadero"];
$query = "SELECT usuario.id, usuario.nombres, usuario.apellidos FROM usuario_parqueadero t_rompimiento 
INNER JOIN usuario ON t_rompimiento.id_usuario = usuario.id WHERE t_rompimiento.id_parqueadero = ".$id_parqueadero;
$response = $connection->query_select($query);
echo json_encode($response);