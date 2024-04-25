<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "";
$query = "SELECT * FROM vehiculo WHERE ";
$length = count($_GET);
$keys = array_keys($_GET); // obtiene los nombres de las varibles
$values = array_values($_GET); // obtiene los valores de las varibles
for ($i = 0; $i < $length; $i++) {
    if ($keys[$i] == "id_propietario") {
        $query .= $keys[$i] . " = " . $values[$i] . " AND ( ";
    } else {
        $query .= "tipo = '" . $values[$i] . "' OR ";
    }
}
$pos = strripos($query, " OR ");
if ($pos) {
    $query = substr($query, 0, $pos);
    $query .= ")";
} else {
    $pos = strripos($query, " AND ");
    $query = substr($query, 0, $pos);
}
$response = $connection->query_select($query);
echo json_encode($response);
