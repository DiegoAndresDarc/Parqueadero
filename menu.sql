-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.14-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando datos para la tabla parqueadero.menu: ~31 rows (aproximadamente)
DELETE FROM `menu`;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` (`id_menu`, `nombre`, `tipo_usuario`, `id_padre`, `tiene_hijos`) VALUES
	(1, 'Administrar copropiedad', 'R', NULL, 1),
	(2, 'Agregar copropiedad', 'R', 1, 0),
	(3, 'Modificar copropiedad', 'R', 1, 0),
	(6, 'Eliminar copropiedad', 'R', 1, 0),
	(7, 'Administrar usuarios', 'R', NULL, 1),
	(8, 'Agregar usuario', 'R', 7, 0),
	(9, 'Modificar usuario', 'R', 7, 0),
	(10, 'Eliminar usuario', 'R', 7, 0),
	(11, 'Administrar copropiedad', 'A', NULL, 1),
	(12, 'Configurar parametros', 'A', 11, 0),
	(13, 'Modificar parametros', 'A', 11, 0),
	(14, 'Administrar parqueaderos', 'A', NULL, 1),
	(15, 'Agregar parqueadero', 'A', 14, 0),
	(16, 'Modificar parqueadero', 'A', 14, 0),
	(17, 'Eliminar parqueadero', 'A', 14, 0),
	(18, 'Administrar usuarios', 'A', NULL, 1),
	(19, 'Agregar usuario', 'A', 18, 0),
	(20, 'Modificar usuario', 'A', 18, 0),
	(21, 'Modificar datos principales', 'A', 20, 0),
	(22, 'Modificar parqueaderos', 'A', 20, 0),
	(23, 'Dar un parqueadero', 'A', 22, 0),
	(24, 'Quitar un parqueadero', 'A', 22, 0),
	(25, 'Eliminar usuario', 'A', 18, 0),
	(26, 'Administrar datos', 'C', NULL, 1),
	(27, 'Modificar datos principales', 'C', 26, 0),
	(28, 'Modificar contraseña', 'C', 26, 0),
	(29, 'Visualizar datos de mis parqueaderos', 'C', NULL, 0),
	(30, 'Entrada de vehiculo', 'G', NULL, 0),
	(31, 'Salida de vehiculo', 'G', NULL, 0);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
