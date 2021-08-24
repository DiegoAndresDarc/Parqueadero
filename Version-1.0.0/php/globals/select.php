<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "";
$length = count($_GET);
$keys = array_keys($_GET); // obtiene los nombres de las varibles
$values = array_values($_GET); // obtiene los valores de las varibles
for ($i = 0; $i < $length; $i++) {
    if ($keys[$i] == "tabla") {
        $tabla = $values[$i];
    } else {
        $condicion[$keys[$i]] = is_numeric($values[$i]) ? $values[$i] : "'" . $values[$i] . "'";
    }
}
$campos = "*";
$response = $connection->select($tabla, $campos, $condicion);
echo json_encode($response);
