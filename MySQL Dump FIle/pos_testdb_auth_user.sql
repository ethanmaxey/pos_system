CREATE DATABASE  IF NOT EXISTS `pos_testdb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `pos_testdb`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: pos-mysql-server.mysql.database.azure.com    Database: pos_testdb
-- ------------------------------------------------------
-- Server version	5.7.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$Ificyd6z5Kt0vKBOnhqwjU$DZAWLE8qnl/W1bYBh3NFreny6PxKmA7I7HnVSBrsOXI=','2022-11-28 02:55:41.434754',1,'admin','admin','someone','admin@somewhere.com',1,1,'2022-11-22 09:55:56.328789'),(2,'pbkdf2_sha256$390000$kksl9JgcLEhtlkc2RPkPzY$3lOQDI53aba5Ha4as9QMjfvtCZDvsFASZIAszOrYvnM=','2022-11-22 22:40:34.905648',0,'johnsmith','John','Smith','johnsmith@gmail.com',0,1,'2022-11-22 22:01:19.442004'),(3,'pbkdf2_sha256$390000$5C1D8pw2BP7pv0Ry0Wc4ZS$CiHtUo3FoQRnr6v1LmHwP9w+T7xd5zbiCFMdyEjEc5o=',NULL,0,'bobj_ones','Bob','Jones','bobjones@gmail.com',0,1,'2022-11-22 22:05:31.838487'),(4,'pbkdf2_sha256$390000$yiZCe4pi75Cox0wB2dkM8h$H4yjNmwu/laMI++y1iEIfbfzzm2sqbtw/DT5fThCNAY=',NULL,0,'jessepinkman','Jesse','Pinkman','jesspinkman@gmail.com',0,1,'2022-11-22 22:07:52.885640'),(5,'pbkdf2_sha256$390000$ACc16KE1WDFLsuVmfa0ZJw$n4Ywsuq9oqwLm2lIlJdMm65oREkOVvoPm0j+pbrOSmc=','2022-11-28 02:04:22.148466',0,'walterwhite','Walter','White','walterwhite@gmail.com',0,1,'2022-11-22 22:08:20.764989'),(6,'pbkdf2_sha256$390000$5xCPseo0v0cAXghp7BSAz8$o9wF+kEO3/DNBA43KagxnunWhxqfLYK7/iNuORCtrwQ=',NULL,0,'skylerwhite','Skyler','White','skylerwhite@gmail.com',0,1,'2022-11-22 22:08:56.352358'),(7,'pbkdf2_sha256$390000$e3tT4DvJB2RoF7FRKQ8gYe$+cf2+bk5NvcY7ztSgNGgJq0AImtekgZ9wjGNJxx+GSM=','2022-11-27 23:56:14.637506',0,'tyler_balka','Tyler','Balka','tyler_balka@gmail.com',1,1,'2022-11-22 23:46:22.695709'),(8,'pbkdf2_sha256$390000$HqeiKuHdT8EcaeNYLn9f2R$lgcGyMjlbtuVW0UFo68bcGuuddPWUJigE/oyx1m/xN0=',NULL,0,'charleshearne','Charles','Hearne','charles@gmail.com',1,1,'2022-11-24 22:04:19.388779'),(9,'pbkdf2_sha256$390000$Y086L4spf2AmOKTciqmYr6$hwG52orhWzX+rbPH2LAwc9j+2WC1iP3LXvA7C2rMPTs=','2022-11-28 02:48:52.052840',0,'pabloramirez','Pablo','Ramirez','pablo@gmail.com',1,1,'2022-11-26 03:16:54.808310'),(10,'pbkdf2_sha256$390000$jJpiooj3FIhucYU8Owym2c$t0ogsmCnkdvi9EqY+u+RfLxaoOKLku7ytxVtIg9vuY0=',NULL,0,'ethan_maxey','Ethan','Maxey','ethan@gmail.com',1,1,'2022-11-26 16:07:32.523048'),(11,'pbkdf2_sha256$390000$B29YV2YxHtW6gOxavKJizE$xrgc4JyjbN1ODleeDtG/abGO0WqXvnonVtVkH9n3dM8=',NULL,0,'robjones','Rob','Jones','rob@gmail.com',0,1,'2022-11-26 16:11:57.505121'),(44,'pbkdf2_sha256$390000$TORSGygf9XrgJlMMvtYTEH$CPTqYLSQO3Uv94E0pnlBtdgDLGBluMiA7lCTspPTzzQ=','2022-11-27 23:54:43.787605',0,'hi','hi','hi','hi@gmail.com',0,1,'2022-11-27 23:54:36.727392');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 21:14:38
