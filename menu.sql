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

-- Volcando datos para la tabla parqueadero.menu: ~40 rows (aproximadamente)
DELETE FROM `menu`;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` (`id_menu`, `id_padre`, `nombre`, `tipo_usuario`, `tiene_hijos`) VALUES
	(1, NULL, 'Administrar copropiedad', 'R', 1),
	(2, 1, 'Agregar copropiedad', 'R', 0),
	(3, 1, 'Modificar copropiedad', 'R', 0),
	(6, 1, 'Eliminar copropiedad', 'R', 0),
	(7, NULL, 'Administrar usuarios', 'R', 1),
	(8, 7, 'Agregar usuario', 'R', 0),
	(9, 7, 'Modificar usuario', 'R', 0),
	(10, 7, 'Eliminar usuario', 'R', 0),
	(11, NULL, 'Administrar copropiedad', 'A', 1),
	(12, 11, 'Configurar parametros', 'A', 0),
	(13, 11, 'Modificar parametros', 'A', 0),
	(14, NULL, 'Administrar apartamentos', 'A', 1),
	(15, 14, 'Agregar apartamento', 'A', 0),
	(16, 14, 'Modificar apartamento', 'A', 0),
	(17, 14, 'Eliminar apartamento', 'A', 0),
	(18, NULL, 'Administrar usuarios', 'A', 1),
	(19, 18, 'Agregar usuario', 'A', 0),
	(20, 18, 'Modificar usuario', 'A', 0),
	(21, 18, 'Eliminar usuario', 'A', 0),
	(22, NULL, 'Administrar vehiculos', 'A', 1),
	(23, 22, 'Agregar vehiculo', 'A', 0),
	(24, 22, 'Modificar vehiculo', 'A', 0),
	(25, 22, 'Eliminar vehiculo', 'A', 0),
	(26, NULL, 'Administrar parqueaderos', 'A', 1),
	(27, 26, 'Agregar parqueadero', 'A', 0),
	(28, 6, 'Modificar parqueadero', 'A', 0),
	(29, 6, 'Eliminar parqueadero', 'A', 0),
	(30, 6, 'Dar un parqueadero', 'A', 0),
	(31, 26, 'Quitar un parqueadero', 'A', 0),
	(32, 26, 'Visualizar parqueadero', 'A', 0),
	(33, NULL, 'Administrar pagos', 'A', 1),
	(34, 33, 'Pago individual', 'A', 0),
	(35, 33, 'Pago multiple', 'A', NULL),
	(36, NULL, 'Iniciar turno', 'G', 0),
	(37, NULL, 'Finalizar turno', 'G', 0),
	(38, NULL, 'Entrada de vehiculo', 'G', 0),
	(39, NULL, 'Salida de vehiculo', 'G', 0),
	(40, NULL, 'Administrar visitante', 'G', 1),
	(41, 40, 'Entrada de visitante', 'G', 0),
	(42, 40, 'Salida de visitante', 'G', 0);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
