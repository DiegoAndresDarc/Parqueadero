<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$datos = array();
$info = file_get_contents('php://input');
$data = json_decode($info);
$query = "UPDATE registro_visitantes SET ";
$condicion = " WHERE fecha_salida IS NULL AND hora_salida IS NULL AND ";
foreach ($data as $clave => $valor) {
    if ($clave == 'id') {
        $condicion .= $clave . " = " . $valor;
    } else {
        $query .= $clave . " = ";
        $query .= is_numeric($valor) ? $valor : "'" . $valor . "'";
        $query .= ",";
        $datos[$clave] = $valor;
    }
}
$pos = strripos($query, ",");
$query = substr($query, 0, $pos);
$query .= $condicion;
$response = $connection->query_update($query);
$url_image = "../documentos/imagen/" . $datos['nombre_responsable'] . "_" . $datos['marca'] . "_" . $datos['color'] . "_visitorVehicleImage.jpeg";
if (file_exists($url_image)) {
    unlink($url_image);
}
echo json_encode($response);
