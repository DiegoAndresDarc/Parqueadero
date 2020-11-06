<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$datos = array();
$tabla = "";
$info = file_get_contents('php://input');
$data = json_decode($info);
foreach ($data as $clave => $valor) {
    if ($clave == 'tabla') {
        $tabla = $valor;
    } else if ($clave == 'id') {
        $condicion[$clave] = $valor;
    } else {
        if ($clave != 'soat' && $clave != 'carta_propiedad' && $clave != 'foto') {
            if (!empty($valor))
                $datos[$clave] = is_numeric($valor) ? $valor : "'" . $valor . "'";
            else {
                $datos[$clave] = 'NULL';
            }
        } else
            $datos[$clave] = $valor;
    }
}
if (isset($datos['soat'])) {
    $url_soat = "../documentos/soat/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_SOAT.pdf";
    $url_soat = str_replace("'", "", $url_soat);
    $soat = base64_decode($datos['soat']);
    $datos['soat'] = "'" . $url_soat . "'";
    if (file_exists($url_soat)) {
        unlink($url_soat);
    }
    file_put_contents($url_soat, $soat);
}
if (isset($datos['carta_propiedad'])) {
    $url_owner = "../documentos/carta_propiedad/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_OwnerShip.pdf";
    $url_owner = str_replace("'", "", $url_owner);
    $owner_ship = base64_decode($datos['carta_propiedad']);
    $datos['carta_propiedad'] = "'" . $url_owner . "'";
    if (file_exists($url_owner)) {
        unlink($url_owner);
    }
    file_put_contents($url_owner, $owner_ship);
}
if (isset($datos['foto'])) {
    $url_image = "../documentos/imagen/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_vehicleImage.jpeg";
    $url_image = str_replace("'", "", $url_image);
    $image = base64_decode($datos['foto']);
    $datos['foto'] = "'" . $url_image . "'";
    if (file_exists($url_image)) {
        unlink($url_image);
    }
    file_put_contents($url_image, $image);
}
$response = $connection->update($tabla, $datos, $condicion);
echo json_encode($response);
