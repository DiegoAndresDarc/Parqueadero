<?php
require "connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "menu";
$tipo_usuario = $_GET['tipo_usuario'];
$campos = "id_menu,id_padre,nombre,tiene_hijos,mostrar";
$condicion['tipo_usuario'] = "'".$tipo_usuario."'";
$response = $connection->select($tabla, $campos, $condicion);
echo json_encode($response);
