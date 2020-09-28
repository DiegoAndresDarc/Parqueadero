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
            or die(mysqli_error());
        $this->conexion->set_charset("utf-8");
    }
    //INSERT
    public function insert($tabla, $datos)
    {
        $result = $this->conexion->query("INSERT INTO $tabla VALUES($datos)") or die($this->conexion->error);
        if ($result)
            return true;
        return false;
    }
    //SELECT
    public function select($tabla, $datos, $condicion)
    {
        $result = $this->conexion->query("SELECT $datos FROM $tabla WHERE $condicion") or die($this->conexion->error);
        if ($result)
            return $result->fetch_all(MYSQLI_ASSOC);
        return $result;
    }
    //UPDATE
    public function UPDATE($tabla, $datos, $condicion)
    {
        $result = $this->conexion->query("UPDATE FROM $tabla SET $datos WHERE $condicion") or die($this->conexion->error);
        if ($result)
            return true;
        return false;
    }
    //DELETE
    public function DELETE($tabla, $condicion)
    {
        $result = $this->conexion->query("DELETE FROM $tabla WHERE $condicion") or die($this->conexion->error);
        if ($result)
            return true;
        return false;
    }
}
