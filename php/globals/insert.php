<?php

require "connection.php";
$connection = new Connection();
$response = array();
$datos = array();
$tabla = "";
$info = file_get_contents('php://input');
$data = json_decode($info);
foreach ($data as $clave => $valor) {
    if ($clave == 'tabla') {
        $tabla = $valor;
    } else {
        $datos[$clave] = is_numeric($valor) ? $valor : "'" . $valor . "'";
    }
}
$response = $connection->insert($tabla, $datos);
echo json_encode($response);
