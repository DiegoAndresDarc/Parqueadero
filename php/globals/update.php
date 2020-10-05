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
    } else if ($clave == 'id') {
        $condicion[$clave] = $valor;
    } else {
        if (!empty($valor))
            $datos[$clave] = is_numeric($valor) ? $valor : "'" . $valor . "'";
    }
}
$response = $connection->update($tabla, $datos, $condicion);
echo json_encode($response);
