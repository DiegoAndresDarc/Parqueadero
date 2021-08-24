-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.17-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla parqueadero.menu
CREATE TABLE IF NOT EXISTS `menu` (
  `id_menu` int(11) NOT NULL AUTO_INCREMENT,
  `id_padre` int(11) DEFAULT NULL,
  `nombre` varchar(50) NOT NULL,
  `tipo_usuario` char(1) NOT NULL,
  `tiene_hijos` tinyint(4) DEFAULT NULL,
  `mostrar` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id_menu`),
  KEY `IXFK_Menu_Menu` (`id_padre`),
  CONSTRAINT `FK_Menu_Menu` FOREIGN KEY (`id_padre`) REFERENCES `menu` (`id_menu`) ON DELETE SET NULL ON UPDATE SET NULL,
  CONSTRAINT `CK_Tipo_usuario` CHECK (`tipo_usuario` in ('A','C','G','R'))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8 COMMENT='Tabla para manejar el arbol de menus de acuerdo al tipo de usuario.';

-- Volcando datos para la tabla parqueadero.menu: ~40 rows (aproximadamente)
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
	(14, NULL, 'Administrar apartamentos', 'A', 1, NULL),
	(15, 14, 'Agregar apartamento', 'A', 0, NULL),
	(16, 14, 'Modificar apartamento', 'A', 0, NULL),
	(17, 14, 'Eliminar apartamento', 'A', 0, NULL),
	(18, NULL, 'Administrar usuarios', 'A', 1, NULL),
	(19, 18, 'Agregar usuario', 'A', 0, NULL),
	(20, 18, 'Modificar usuario', 'A', 0, NULL),
	(21, 18, 'Eliminar usuario', 'A', 0, NULL),
	(22, NULL, 'Administrar vehiculos', 'A', 1, NULL),
	(23, 22, 'Agregar vehiculo', 'A', 0, NULL),
	(24, 22, 'Modificar vehiculo', 'A', 0, NULL),
	(25, 22, 'Eliminar vehiculo', 'A', 0, NULL),
	(26, NULL, 'Administrar parqueaderos', 'A', 1, NULL),
	(27, 26, 'Agregar parqueadero', 'A', 0, NULL),
	(28, 26, 'Modificar parqueadero', 'A', 0, NULL),
	(29, 26, 'Eliminar parqueadero', 'A', 0, NULL),
	(30, 26, 'Dar un parqueadero', 'A', 0, NULL),
	(31, 26, 'Quitar un parqueadero', 'A', 0, NULL),
	(32, 26, 'Visualizar parqueadero', 'A', 0, NULL),
	(33, NULL, 'Administrar pagos', 'A', 1, NULL),
	(34, 33, 'Pago individual', 'A', 0, NULL),
	(35, 33, 'Pago multiple', 'A', NULL, NULL),
	(36, NULL, 'Iniciar turno', 'G', 0, NULL),
	(37, NULL, 'Finalizar turno', 'G', 0, NULL),
	(38, NULL, 'Entrada de vehiculo', 'G', 0, NULL),
	(39, NULL, 'Salida de vehiculo', 'G', 0, NULL),
	(40, NULL, 'Administrar visitante', 'G', 1, NULL),
	(41, 40, 'Entrada de visitante', 'G', 0, NULL),
	(42, 40, 'Salida de visitante', 'G', 0, NULL),
	(43, NULL, 'Arqueo de caja', 'G', 0, NULL);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
