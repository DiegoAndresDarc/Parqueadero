<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$datos = array();
$tabla = "";
$length = count($_FILES);
$values = array_values($_FILES); // obtiene los valores de las varibles
for ($i = 0; $i < $length; $i++) {
    $datos[$i] = $values[$i];
}
echo json_encode($datos);
