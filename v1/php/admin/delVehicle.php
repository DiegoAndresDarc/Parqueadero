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
    }
    if ($clave == 'id') {
        $condicion[$clave] = $valor;
    } else
        $datos[$clave] = $valor;
}
$url_soat = "../documentos/soat/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_SOAT.pdf";
//$url_soat = str_replace("'", "", $url_soat);
if (file_exists($url_soat)) {
    unlink($url_soat);
}

$url_owner = "../documentos/carta_propiedad/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_OwnerShip.pdf";
//$url_owner = str_replace("'", "", $url_owner);
if (file_exists($url_owner)) {
    unlink($url_owner);
}

$url_image = "../documentos/imagen/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_vehicleImage.jpeg";
//$url_image = str_replace("'", "", $url_image);
if (file_exists($url_image)) {
    unlink($url_image);
}
$response = $connection->delete($tabla, $condicion);
echo json_encode($response);
