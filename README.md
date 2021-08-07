# cars_game 


# crear base de datos

CREATE DATABASE `cars_game` /*!40100 DEFAULT CHARACTER SET utf8 */;

# crear tabla juegos

CREATE TABLE `juegos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `primero` varchar(255) DEFAULT NULL,
  `segundo` varchar(255) DEFAULT NULL,
  `tercero` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

# crear tabla jugadores

CREATE TABLE `jugadores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
