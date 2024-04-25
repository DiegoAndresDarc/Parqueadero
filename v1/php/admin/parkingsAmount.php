<?php
require "../connection.php";
$connection = new Connection();
$response = array();
$condicion = array();
$tabla = "";
$id_copropiedad = $_GET["id_copropiedad"];
$query = "SELECT COUNT(admite_carro) AS CANTIDAD FROM parqueadero WHERE tipo = 'RESIDENTE' AND id_copropiedad = " . $id_copropiedad . " UNION ALL ";
$query .= "SELECT COUNT(admite_moto) AS CANTIDAD FROM parqueadero WHERE tipo = 'RESIDENTE' AND id_copropiedad = " . $id_copropiedad . " UNION ALL ";
$query .= "SELECT COUNT(admite_bicicleta) AS CANTIDAD FROM parqueadero WHERE tipo = 'RESIDENTE' AND id_copropiedad = " . $id_copropiedad . " UNION ALL ";
$query .= "SELECT COUNT(admite_carro) AS CANTIDAD FROM parqueadero WHERE tipo = 'VISITANTE' AND id_copropiedad = " . $id_copropiedad . " UNION ALL ";
$query .= "SELECT COUNT(admite_moto) AS CANTIDAD FROM parqueadero WHERE tipo = 'VISITANTE' AND id_copropiedad = " . $id_copropiedad . " UNION ALL ";
$query .= "SELECT COUNT(admite_bicicleta) AS CANTIDAD FROM parqueadero WHERE tipo = 'VISITANTE' AND id_copropiedad = " . $id_copropiedad;

$response["parqueaderos"] = $connection->query_select($query);

$query = "SELECT n_parqueaderos_carro, n_parqueaderos_moto, n_parqueaderos_bicicleta, n_parqueaderos_carro_vis, n_parqueaderos_moto_vis, n_parqueaderos_bicicleta_vis
 FROM configuraciones WHERE id_copropiedad = " . $id_copropiedad;
$response["copropiedad"] = $connection->query_select($query);
echo json_encode($response);
