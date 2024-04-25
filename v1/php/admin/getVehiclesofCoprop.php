<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$id_copropiedad = $_GET["id_copropiedad"];
$query = "SELECT usuario.nombres, usuario.apellidos, vehiculo.placa, vehiculo.fecha_vencimiento_soat FROM vehiculo 
            INNER JOIN usuario ON vehiculo.id_propietario = usuario.id INNER JOIN copropiedad ON usuario.id_copropiedad = copropiedad.id
            WHERE copropiedad.id = ".$id_copropiedad." AND usuario.tipo_usuario = 'R'";
$response = $connection->query_select($query);
echo json_encode($response);