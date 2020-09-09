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

-- Volcando datos para la tabla parqueadero.menu: ~0 rows (aproximadamente)
DELETE FROM `menu`;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` (`id`, `nombre`, `tipo_usuario`, `id_padre`) VALUES
	(1, 'Administrar copropiedad', 'R', NULL),
	(2, 'Agregar copropiedad', 'R', 1),
	(3, 'Modificar copropiedad', 'R', 1),
	(4, 'Modificar datos principales', 'R', 3),
	(5, 'Modificar administrador', 'R', 3),
	(6, 'Eliminar copropiedad', 'R', 1),
	(7, 'Administrar usuarios', 'R', NULL),
	(8, 'Agregar usuario', 'R', 7),
	(9, 'Modificar usuario', 'R', 7),
	(10, 'Eliminar usuario', 'R', 7),
	(11, 'Administrar copropiedad', 'A', NULL),
	(12, 'Configurar parametros', 'A', 11),
	(13, 'Modificar parametros', 'A', 11),
	(14, 'Administrar parqueaderos', 'A', NULL),
	(15, 'Agregar parqueadero', 'A', 14),
	(16, 'Modificar parqueadero', 'A', 14),
	(17, 'Eliminar parqueadero', 'A', 14),
	(18, 'Administrar usuarios', 'A', NULL),
	(19, 'Agregar usuario', 'A', 18),
	(20, 'Modificar usuario', 'A', 18),
	(21, 'Modificar datos principales', 'A', 20),
	(22, 'Modificar parqueaderos', 'A', 20),
	(23, 'Dar un parqueadero', 'A', 22),
	(24, 'Quitar un parqueadero', 'A', 22),
	(25, 'Eliminar usuario', 'A', 18),
	(26, 'Administrar datos', 'C', NULL),
	(27, 'Modificar datos principales', 'C', 26),
	(28, 'Modificar contraseña', 'C', 26),
	(29, 'Visualizar datos de mis parqueaderos', 'C', NULL),
	(30, 'Entrada de vehiculo', 'G', NULL),
	(31, 'Salida de vehiculo', 'G', NULL);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
