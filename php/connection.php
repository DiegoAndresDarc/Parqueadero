<?php
class Connection
{
    private $host = "localhost";
    private $usuario = "root";
    private $clave = "";
    private $db = "parqueadero";
    public $conexion;
    public function __construct()
    {
        $this->conexion = new mysqli($this->host, $this->usuario, $this->clave, $this->db)
            or die(mysqli_error($this->conexion));
        $this->conexion->set_charset("utf-8");
    }
    //INSERT
    public function insert($tabla, $datos)
    {
        $query = "INSERT INTO $tabla (";
        $values = 'VALUES (';
        foreach ($datos as $clave => $valor) {
            $query .= $clave . ',';
            $values .= $valor . ',';
        }
        $pos = strripos($query, ",");
        $query = substr($query, 0, $pos);
        $query .= ') ';
        $pos = strripos($values, ",");
        $values = substr($values, 0, $pos);
        $values .= ') ';
        $query .= $values;
        $result = $this->conexion->query($query) or die($this->conexion->error);
        if ($result)
            return true;
        return false;
    }
    //SELECT
    public function select($tabla, $campos, $condicion)
    {
        $query = "SELECT $campos FROM $tabla";
        if (count($condicion) > 0) {
            $query .= " WHERE ";
            foreach ($condicion as $clave => $valor) {
                $query .= $clave . " = " . $valor . " AND ";
            }
            $pos = strripos($query, " AND ");
            $query = substr($query, 0, $pos);
        }
        //echo $query;
        $result = $this->conexion->query($query) or die($this->conexion->error);
        if ($result) {
            return $result->fetch_all(MYSQLI_ASSOC);
        }
        return $result;
    }
    //UPDATE
    public function update($tabla, $datos, $condicion)
    {
        $query = "UPDATE $tabla SET ";
        foreach ($datos as $clave => $valor) {
            $query .= $clave . " = " . $valor . ",";
        }
        $pos = strripos($query, ",");
        $query = substr($query, 0, $pos);
        $query .= " WHERE ";
        foreach ($condicion as $clave => $valor) {
            $query .= $clave . " = " . $valor . " AND ";
        }
        $pos = strripos($query, " AND ");
        $query = substr($query, 0, $pos);
        $result = $this->conexion->query($query) or die($this->conexion->error);
        if ($result)
            return true;
        return false;
    }
    //DELETE
    public function delete($tabla, $condicion)
    {
        $query = "DELETE FROM $tabla WHERE ";
        foreach ($condicion as $clave => $valor) {
            $query .= $clave . " = " . $valor . " AND ";
        }
        $pos = strripos($query, " AND ");
        $query = substr($query, 0, $pos);
        $result = $this->conexion->query($query) or die($this->conexion->error);
        if ($result)
            return true;
        return false;
    }

    //QUERY SELECT
    public function query_select($query)
    {
        $result = $this->conexion->query($query) or die($this->conexion->error);
        if ($result) {
            return $result->fetch_all(MYSQLI_ASSOC);
        }
        return $result;
    }
    public function getpassword()
    {
        return $this->clave;
    }
}
