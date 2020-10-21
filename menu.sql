-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.14-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando datos para la tabla parqueadero.menu: ~41 rows (aproximadamente)
DELETE FROM `menu`;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` (`id_menu`, `id_padre`, `nombre`, `tipo_usuario`, `tiene_hijos`, `mostrar`) VALUES
	(1, NULL, 'Administrar copropiedad', 'R', 1, NULL),
	(2, 1, 'Agregar copropiedad', 'R', 0, NULL),
	(3, 1, 'Modificar copropiedad', 'R', 0, NULL),
	(6, 1, 'Eliminar copropiedad', 'R', 0, NULL),
	(7, NULL, 'Administrar usuarios', 'R', 1, NULL),
	(8, 7, 'Agregar usuario', 'R', 0, NULL),
	(9, 7, 'Modificar usuario', 'R', 0, NULL),
	(10, 7, 'Eliminar usuario', 'R', 0, NULL),
	(11, NULL, 'Administrar copropiedad', 'A', 1, NULL),
	(12, 11, 'Configurar parametros', 'A', 0, NULL),
	(13, 11, 'Modificar parametros', 'A', 0, NULL),
	(14, NULL, 'Administrar parqueaderos', 'A', 1, NULL),
	(15, 14, 'Agregar parqueadero', 'A', 0, NULL),
	(16, 14, 'Modificar parqueadero', 'A', 0, NULL),
	(17, 14, 'Eliminar parqueadero', 'A', 0, NULL),
	(18, NULL, 'Administrar usuarios', 'A', 1, NULL),
	(19, 18, 'Agregar usuario', 'A', 0, NULL),
	(20, 18, 'Modificar usuario', 'A', 0, NULL),
	(21, 20, 'Modificar datos principales', 'C', 0, NULL),
	(23, 14, 'Dar un parqueadero', 'A', 0, NULL),
	(24, 14, 'Quitar un parqueadero', 'A', 0, NULL),
	(25, 18, 'Eliminar usuario', 'A', 0, NULL),
	(26, NULL, 'Administrar datos', 'C', 1, NULL),
	(27, 26, 'Modificar datos principales', 'C', 0, NULL),
	(28, 26, 'Modificar contraseña', 'C', 0, NULL),
	(29, NULL, 'Visualizar datos de mis parqueaderos', 'C', 0, NULL),
	(30, NULL, 'Entrada de vehiculo', 'G', 0, NULL),
	(31, NULL, 'Salida de vehiculo', 'G', 0, NULL),
	(33, NULL, 'Administrar apartamentos', 'A', 1, NULL),
	(34, 33, 'Agregar apartamento', 'A', 0, NULL),
	(35, 33, 'Modificar apartamento', 'A', 0, NULL),
	(36, 33, 'Eliminar apartamento', 'A', 0, NULL),
	(37, NULL, 'Administrar visitante', 'G', 1, NULL),
	(38, 37, 'Entrada de visitante', 'G', 0, NULL),
	(39, 37, 'Salida de visitante', 'G', 0, NULL),
	(40, NULL, 'Iniciar turno', 'G', 0, NULL),
	(41, NULL, 'Finalizar turno', 'G', 0, NULL),
	(42, NULL, 'Administrar vehiculos', 'A', 1, NULL),
	(43, 42, 'Agregar vehiculo', 'A', 0, NULL),
	(44, 42, 'Modificar vehiculo', 'A', 0, NULL),
	(45, 42, 'Eliminar vehiculo', 'A', 0, NULL);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
