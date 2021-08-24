<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$datos = array();
$condicion = array();
$tabla = "";
$info = file_get_contents('php://input');
$data = json_decode($info);
foreach ($data as $clave => $valor) {
    if ($clave == 'tabla') {
        $tabla = $valor;
    } else {
        $condicion[$clave] = $valor;
    }
}
$response = $connection->delete($tabla, $condicion);
echo json_encode($response);
