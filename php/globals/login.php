<?php
require "connection.php";
$connection = new Connection();
$response = array();
$datos = array();
$condicion = array();
if (isset($_POST['usuario']) && isset($_POST['password'])) {
    $tabla = "usuario";
    $usuario = $_POST['usuario'];
    $password = $_POST['password'];
    $campos = "id,nombres,apellidos,tipo_usuario";
    $condicion['usuario'] = $usuario;
    $condicion['password'] = $password;
    $response = $connection->select($tabla, $campos, $condicion);
}
echo json_encode($response);
