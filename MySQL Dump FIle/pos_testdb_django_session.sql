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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bunigtbj36ynqsltsl0zrt4ntlg7kz2n','.eJxVjDsOwjAQBe_iGll2FmKbkp4zRPszDiBHipMKcXeIlALaNzPvZQZclzKsTedhFHM23hx-N0J-aN2A3LHeJstTXeaR7KbYnTZ7nUSfl939OyjYyrfmnkJiF1yiFNwJnKAeXSSfcwRIQTMQinesnfSsEZkJYpc8AEgWMO8P6PY4XA:1ozP7n:IZYUY3hA_khqNdmuQ4WRroc6kjOBtGU9aVzOtsPKZBM','2022-12-11 21:23:43.129000'),('iqdwee036qwerycb3c98mp28fcrtkayk','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMN5ffjZDfOhxAXjg8R8vjUKae7KHYk872MYp-7qf7F-hw7vY31xQSu-ASpeBu4AT16iL5nCNACpqBULxjraRmjchMEKvkAUCywB5lnIpp1m37AitnO6g:1ozRZB:pLbjvett2jzt7t62y2PEnyWuL2tXBQF3VHAbyDC2OHg','2022-12-12 00:00:09.336829'),('nka78s7c3jp6xmmevjpzurmdvsjwbpdb','.eJxdjrEOgzAQQ__lZhQlHJCEsXu_AV0uodBW0EIYKsS_l0gMpYsH-9nyCg0tsWuWOUxN76EGBdmv54gfYUiBv9NwGwWPQ5x6JxIijnQW19GH5-VgTwMdzd3e5sppy1JL66yWJUpPoZDGqbY1iFaHFh15JTnkvuJgiNmhya1CRN963EeZpgj1CqpI-l5oiH38QJ1n8Jp6Dum8sBa2DFR5RtQ_sm1f5BRPjA:1ozR7O:7PO_CA9SbR3svgkHuUDkJ0fTUN0fYQFFareW3KEs8Dc','2022-12-11 23:31:26.869015'),('oqtpgj6uuq3687kppgxq5ey737fttdst','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMT-byOxLyW4eDyAuH52h5HMrUkz0Ue9LZPkbRz_10_wIdzt3-5ppCYhdcohTcDZygXl0kn3MESEEzEIp3rJXUrBGZCWKVPABIFtijjFMxzbptX1ZaO-E:1oxciF:3GNlnIf1_eZIRr-nDUJ6SG6Hzhmfc8KNChjRwt35i4c','2022-12-06 23:29:59.465516'),('pfief437zw77fq3968mcel9k4xk1je69','.eJxVjrEOgzAQQ__lZhQlHBDC2L3fgC6Xo9BW0EIYKsS_l0gM7eLBfra8QUtr7Nt1kbkdAjRgIPv1PPFDxhSEO423SfE0xnnwKiHqTBd1nYI8Lyf7N9DT0h9trrx1rK123lldog4kha696boa0Vnp0FMwmiUPFUtNzB7r3BlEDF3AY5RpjtBsYMqk75XGOMQPNEUGr3lgSeeVc7Dv-xe64EWH:1ozA5d:ym1o5d1tEKGHCmq70B3QMmqyUEkRUXj3wCj3rVTC05I','2022-12-11 05:20:29.972571'),('r4vq4x2i5zeqih8ot9jwuyoh9rur013i','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMT-byOxLyW4eDyAuH52h5HMrUkz0Ue9LZPkbRz_10_wIdzt3-5ppCYhdcohTcDZygXl0kn3MESEEzEIp3rJXUrBGZCWKVPABIFtijjFMxzbptX1ZaO-E:1oxa4Y:6s5ljn5BvXh6F6ZukLxyi8kaUsZQLYRfGTnle6bjat8','2022-12-06 20:40:50.253014'),('s37w2nocd7d1s188pskcymsltdfqyn94','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMN5ffjZDfOhxAXjg8R8vjUKae7KHYk872MYp-7qf7F-hw7vY31xQSu-ASpeBu4AT16iL5nCNACpqBULxjraRmjchMEKvkAUCywB5lnIpp1m37AitnO6g:1ozUU8:xdXRQA8l3AhO23FDZM_0Sk0Sxt1-eOrNfsD-NE8CNzI','2022-12-12 03:07:08.692829'),('v6hf43kk3libzwp3l7z5qg479upnwqrr','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMN5ffjZDfOhxAXjg8R8vjUKae7KHYk872MYp-7qf7F-hw7vY31xQSu-ASpeBu4AT16iL5nCNACpqBULxjraRmjchMEKvkAUCywB5lnIpp1m37AitnO6g:1ozRFL:jVwzpTkikwajWyXiJyYbhB0eifb-bxocHJgouPQetgw','2022-12-11 23:39:39.397462'),('vh1kc98q7d6jxd2ii800bb6uv7psse6s','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMN5ffjZDfOhxAXjg8R8vjUKae7KHYk872MYp-7qf7F-hw7vY31xQSu-ASpeBu4AT16iL5nCNACpqBULxjraRmjchMEKvkAUCywB5lnIpp1m37AitnO6g:1ozRWQ:cMva5M5yaPQpmQr7JDrCf1Js1N_ntp2Vhira0WobKGE','2022-12-11 23:57:18.721427'),('zah0ipl0qr1sbb3l03d8os5m4268mmhz','.eJxVjsEOgjAQRP9lz6RpXYSWo3e_gWx3i1QNaCkHQ_h3IeGglznMvJnMAi3NuW_nKaQ2CjRgoPj1PPEjDHsgdxpuo-JxyCl6tSPqSCd1HSU8Lwf7N9DT1G9trnztWNfaeVfrM2qhUGrrTddZRFeHDj2J0RxOUnGwxOzRnpxBROkEt1GmlKFZwJS7vmcacswfaLCAV4oc9vPKOVjX9Qu6q0WF:1ozQbH:ybeTnFrh3gdufs2OQMVMqJ2DmrNgj78V2U6ijKjQ2bQ','2022-12-11 22:58:15.125653'),('zk4c76k6jyrfc1vy1iq2020ull1otcsm','.eJxVjMsOgjAUBf-la9O0XKUtS_d-A7mvCmoggbIi_LuQsNDtmTmzmhaX0rXLrFPbi2mMN5ffjZDfOhxAXjg8R8vjUKae7KHYk872MYp-7qf7F-hw7vY31xQSu-ASpeBu4AT16iL5nCNACpqBULxjraRmjchMEKvkAUCywB5lnIpp1m37AitnO6g:1ozUbH:qZQgBsHQazN4mTKysnguFMKs644FW_SD22ElAU-XSWk','2022-12-12 03:14:31.749279');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 21:14:34
