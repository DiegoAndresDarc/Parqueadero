<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "";
$length = count($_GET);
$keys = array_keys($_GET); // obtiene los nombres de las varibles
$values = array_values($_GET); // obtiene los valores de las varibles
$query = "SELECT vehiculo.id,vehiculo.foto,vehiculo.fecha_vencimiento_soat FROM vehiculo WHERE ";
for ($i = 0; $i < $length; $i++) {
    if ($keys[$i] == "id_propietario" || $keys[$i] == "id_parqueadero") {
        $query .= $keys[$i] . " = " . $values[$i] . " AND ";
    }
}

$pos = strripos($query, " AND ");
$query = substr($query, 0, $pos);
$response = $connection->query_select($query);
echo json_encode($response);
