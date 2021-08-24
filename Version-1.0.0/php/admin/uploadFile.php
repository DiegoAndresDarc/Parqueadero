<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$fileData = array();
$tabla = "";
$length = count($_FILES);
$values = array_values($_FILES); // obtiene los valores de las varibles
for ($i = 0; $i < $length; $i++) {
    $fileData[$i] = $values[$i];
}

$linea = 0;
//Abrimos nuestro archivo
$archivo = fopen($fileData[0]['tmp_name'], "r");
//Lo recorremos
while (($datos = fgetcsv($archivo, 0, ";")) == true) {
    $num = count($datos);
    if (!is_numeric($datos[0])) {
        continue;
    }
    $query = "SELECT id FROM usuario WHERE identificacion = " . $datos[0];
    $queryResponse = $connection->query_select($query);
    if ($queryResponse) {
        $id_usuario = $queryResponse[0]['id'];
        $query = "SELECT id FROM parqueadero WHERE codigo = '" . $datos[1] . "' AND id_usuario = " . $id_usuario;
        $queryResponse = $connection->query_select($query);
        if ($queryResponse) {
            $campos = array();
            $campos['id_usuario'] = $id_usuario;
            $campos['id_parqueadero'] = $queryResponse[0]['id'];
            $campos['fecha_pago'] = "'" . $datos[2] . "'";
            $campos['hora_pago'] = "'" . $datos[3] . "'";
            $response = $connection->insert("pagos", $campos);
        } else {
            $response[$linea]['usuario'] = $datos[0];
            $response[$linea]['parqueadero'] = $datos[1];
            $linea++;
        }
    } else {
        $response['usuario'] = $datos[0];
        $response[$linea]['parqueadero'] = $datos[1];
        $linea++;
    }
}
//Cerramos el archivo
fclose($archivo);
echo json_encode($response);
