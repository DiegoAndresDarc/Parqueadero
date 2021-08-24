<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$info = file_get_contents('php://input');
$data = json_decode($info);
$query = "UPDATE turno SET ";
$condicion = " WHERE fecha_salida IS NULL AND hora_salida IS NULL AND ";
foreach ($data as $clave => $valor) {
    if ($clave == 'id_usuario') {
        $condicion .= $clave . " = " . $valor;
    } else {
        $query .= $clave . " = ";
        $query .= is_numeric($valor) ? $valor : "'" . $valor . "'";
        $query .= ",";
    }
}
$pos = strripos($query, ",");
$query = substr($query, 0, $pos);
$query .= $condicion;
$response = $connection->query_update($query);
echo json_encode($response);
