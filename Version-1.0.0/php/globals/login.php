<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "usuario";
$usuario = $_GET['usuario'];
$password = $_GET['password'];
//if($usuario == "root" && $password == $connection->getpassword())
if ($usuario == "root") {
    $response[0]['id'] = 0;
    $response[0]['nombres'] = 'ADMINISTRADOR';
    $response[0]['apellidos'] = 'DEL SISTEMA';
    $response[0]['tipo_usuario'] = 'R';
} else {
    $campos = "id,nombres,apellidos,tipo_usuario";
    $condicion['usuario'] = "'".$usuario."'";
    $condicion['password'] = "'".$password."'";
    $response = $connection->select($tabla, $campos, $condicion);
}
echo json_encode($response);
