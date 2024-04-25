<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$datos = array();
$files = array();
$tabla = "";
$info = file_get_contents('php://input');
$data = json_decode($info);
foreach ($data as $clave => $valor) {
    if ($clave == 'tabla') {
        $tabla = $valor;
    } else {
        if ($clave != 'soat' && $clave != 'carta_propiedad' && $clave != 'foto')
            $datos[$clave] = is_numeric($valor) ? $valor : "'" . $valor . "'";
        else
            $datos[$clave] = $valor;
    }
}
if (isset($datos['visitante'])) {
    $url_image = "../documentos/imagen/" . $datos['nombre_responsable'] . "_" . $datos['marca'] . "_" . $datos['color'] . "_visitorVehicleImage.jpeg";
    $url_image = str_replace("'", "", $url_image);
    unset($datos['visitante']);
} else {
    $url_soat = "../documentos/soat/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_SOAT.pdf";
    $url_owner = "../documentos/carta_propiedad/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_OwnerShip.pdf";
    $url_image = "../documentos/imagen/" . $datos['id_propietario'] . "_" . $datos['marca'] . "_" . $datos['modelo'] . "_" . $datos['color'] . "_vehicleImage.jpeg";
    $url_soat = str_replace("'", "", $url_soat);
    $url_owner = str_replace("'", "", $url_owner);
    $url_image = str_replace("'", "", $url_image);
    $soat = base64_decode($datos['soat']);
    $owner_ship = base64_decode($datos['carta_propiedad']);

    $datos['soat'] = "'" . $url_soat . "'";
    $datos['carta_propiedad'] = "'" . $url_owner . "'";
}
$image = base64_decode($datos['foto']);
$datos['foto'] = "'" . $url_image . "'";

$response = $connection->insert($tabla, $datos);
if ($response) {
    if (isset($url_soat))
        file_put_contents($url_soat, $soat);
    if (isset($url_owner))
        file_put_contents($url_owner, $owner_ship);
    file_put_contents($url_image, $image);
}

echo json_encode($response);
