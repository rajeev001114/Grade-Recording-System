-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ADM_academic_session`
--

DROP TABLE IF EXISTS `ADM_academic_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_academic_session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(20) NOT NULL,
  `semester` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_academic_session`
--

LOCK TABLES `ADM_academic_session` WRITE;
/*!40000 ALTER TABLE `ADM_academic_session` DISABLE KEYS */;
INSERT INTO `ADM_academic_session` VALUES (10,'2014-15',2,0),(11,'2015-16',1,1);
/*!40000 ALTER TABLE `ADM_academic_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_all_course`
--

DROP TABLE IF EXISTS `ADM_all_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_all_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_code` varchar(10) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `dpname_id` varchar(50),
  PRIMARY KEY (`id`),
  KEY `ADM_all_course_d8c85924` (`dpname_id`),
  CONSTRAINT `dpname_id_33d9b7776d1e2d35_fk_ADM_all_deprtment_department_name` FOREIGN KEY (`dpname_id`) REFERENCES `ADM_all_deprtment` (`department_name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_all_course`
--

LOCK TABLES `ADM_all_course` WRITE;
/*!40000 ALTER TABLE `ADM_all_course` DISABLE KEYS */;
INSERT INTO `ADM_all_course` VALUES (10,'CS 101','Computer Programming and Utilization',0,'Computer Science'),(11,'CS 213','Data Structures and Algorithms',1,'Computer Science'),(14,'CE 201','Fluid Mechanics',1,'Civil Engineering'),(15,'CE 205','Solid Mechanics',1,'Civil Engineering'),(16,'EE 224','Communication Systems',1,'Electrical Engineering'),(17,'EE 308','Digital Systems',1,'Electrical Engineering'),(18,'CS 215','Data Interpretation and Analysis',1,'Computer Science'),(19,'CS 601','Algorithms',1,'Computer Science'),(20,'ME 209','Thermodynamics',1,'Mechanical  Engineering');
/*!40000 ALTER TABLE `ADM_all_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_all_deprtment`
--

DROP TABLE IF EXISTS `ADM_all_deprtment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_all_deprtment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(50) NOT NULL,
  `department_abb` varchar(10) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ADM_all_deprtment_department_name_6fdd5cfe88632217_uniq` (`department_name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_all_deprtment`
--

LOCK TABLES `ADM_all_deprtment` WRITE;
/*!40000 ALTER TABLE `ADM_all_deprtment` DISABLE KEYS */;
INSERT INTO `ADM_all_deprtment` VALUES (3,'Computer Science','CS',1),(6,'Civil Engineering','CE',1),(7,'Electrical Engineering','EE',1),(8,'Chemical Engineering','CHE',1),(10,'Mechanical  Engineering','ME',1);
/*!40000 ALTER TABLE `ADM_all_deprtment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_course_mapping`
--

DROP TABLE IF EXISTS `ADM_course_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_course_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mdl_cid` varchar(20) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `cid_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ADM_course_mapping_cid_id_3e3feaf000c63a4_fk_ADM_all_course_id` (`cid_id`),
  CONSTRAINT `ADM_course_mapping_cid_id_3e3feaf000c63a4_fk_ADM_all_course_id` FOREIGN KEY (`cid_id`) REFERENCES `ADM_all_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_course_mapping`
--

LOCK TABLES `ADM_course_mapping` WRITE;
/*!40000 ALTER TABLE `ADM_course_mapping` DISABLE KEYS */;
INSERT INTO `ADM_course_mapping` VALUES (1,'5',1,20),(2,'3',1,11),(3,'4',1,19),(4,'2',1,10);
/*!40000 ALTER TABLE `ADM_course_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_moodle`
--

DROP TABLE IF EXISTS `ADM_moodle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_moodle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_moodle`
--

LOCK TABLES `ADM_moodle` WRITE;
/*!40000 ALTER TABLE `ADM_moodle` DISABLE KEYS */;
INSERT INTO `ADM_moodle` VALUES (1,0);
/*!40000 ALTER TABLE `ADM_moodle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_student_mapping`
--

DROP TABLE IF EXISTS `ADM_student_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_student_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mdl_id` varchar(20) NOT NULL,
  `mooc_id` varchar(20) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_student_mapping`
--

LOCK TABLES `ADM_student_mapping` WRITE;
/*!40000 ALTER TABLE `ADM_student_mapping` DISABLE KEYS */;
INSERT INTO `ADM_student_mapping` VALUES (1,'2','13305002',1),(2,'3','133005003',1),(3,'4','13305004',1),(4,'5','13305005',1),(5,'6','13305006',1);
/*!40000 ALTER TABLE `ADM_student_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_teacher_mapping`
--

DROP TABLE IF EXISTS `ADM_teacher_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_teacher_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mdl_id` varchar(20) NOT NULL,
  `mooc_id` varchar(20) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_teacher_mapping`
--

LOCK TABLES `ADM_teacher_mapping` WRITE;
/*!40000 ALTER TABLE `ADM_teacher_mapping` DISABLE KEYS */;
INSERT INTO `ADM_teacher_mapping` VALUES (1,'2','1',1),(2,'3','2',1),(3,'4','104',1),(4,'5','105',1),(5,'6','106',1);
/*!40000 ALTER TABLE `ADM_teacher_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_userlogin`
--

DROP TABLE IF EXISTS `ADM_userlogin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_userlogin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usertypeid` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `nooflogins` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `ADM_userlogin_user_id_ca0ac3fc60b3887_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_userlogin`
--

LOCK TABLES `ADM_userlogin` WRITE;
/*!40000 ALTER TABLE `ADM_userlogin` DISABLE KEYS */;
INSERT INTO `ADM_userlogin` VALUES (2,0,1,'2016-05-19 18:55:22',202,4),(3,1,1,'2015-10-05 09:19:21',23,5),(4,1,1,'2016-05-12 08:35:44',146,6);
/*!40000 ALTER TABLE `ADM_userlogin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_bm_grade_policy`
--

DROP TABLE IF EXISTS `MSG_bm_grade_policy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_bm_grade_policy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `min_count` int(11) NOT NULL,
  `weight` double NOT NULL,
  `examtype` varchar(50) NOT NULL,
  `drop_count` int(11) NOT NULL,
  `short_label` varchar(20) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MSG_bm__personid_id_77998ea67f54bbf1_fk_TCH_personinformation_id` (`personid_id`),
  KEY `MSG_bm_g_sessionid_id_ccc73cb93eef367_fk_ADM_academic_session_id` (`sessionid_id`),
  CONSTRAINT `MSG_bm_g_sessionid_id_ccc73cb93eef367_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`),
  CONSTRAINT `MSG_bm__personid_id_77998ea67f54bbf1_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_bm_grade_policy`
--

LOCK TABLES `MSG_bm_grade_policy` WRITE;
/*!40000 ALTER TABLE `MSG_bm_grade_policy` DISABLE KEYS */;
INSERT INTO `MSG_bm_grade_policy` VALUES (1,'Thermodynamics',7,0.6,'Graded Quiz',1,'GQ',2,11),(2,'Thermodynamics',1,0.4,'Final Exam',0,'FE',2,11);
/*!40000 ALTER TABLE `MSG_bm_grade_policy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_bm_max_marks`
--

DROP TABLE IF EXISTS `MSG_bm_max_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_bm_max_marks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `all_eval` varchar(20) NOT NULL,
  `max_marks` int(11) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MSG_bm__personid_id_2a2aae13cfef7341_fk_TCH_personinformation_id` (`personid_id`),
  KEY `MSG_bm__sessionid_id_7d03e046377f6357_fk_ADM_academic_session_id` (`sessionid_id`),
  CONSTRAINT `MSG_bm__personid_id_2a2aae13cfef7341_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`),
  CONSTRAINT `MSG_bm__sessionid_id_7d03e046377f6357_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_bm_max_marks`
--

LOCK TABLES `MSG_bm_max_marks` WRITE;
/*!40000 ALTER TABLE `MSG_bm_max_marks` DISABLE KEYS */;
INSERT INTO `MSG_bm_max_marks` VALUES (163,'Thermodynamics','GQ-1',10,2,11),(164,'Thermodynamics','GQ-2',10,2,11),(165,'Thermodynamics','GQ-3',15,2,11),(166,'Thermodynamics','GQ-4',15,2,11),(167,'Thermodynamics','GQ-5',15,2,11),(168,'Thermodynamics','GQ-6',20,2,11),(169,'Thermodynamics','GQ-7',25,2,11),(170,'Thermodynamics','FE',40,2,11);
/*!40000 ALTER TABLE `MSG_bm_max_marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_bm_policy_weight`
--

DROP TABLE IF EXISTS `MSG_bm_policy_weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_bm_policy_weight` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `pweight` longtext NOT NULL,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MSG_bm__personid_id_115f356275ae2817_fk_TCH_personinformation_id` (`personid_id`),
  KEY `MSG_bm_p_sessionid_id_550c664defb8da1_fk_ADM_academic_session_id` (`sessionid_id`),
  CONSTRAINT `MSG_bm_p_sessionid_id_550c664defb8da1_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`),
  CONSTRAINT `MSG_bm__personid_id_115f356275ae2817_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_bm_policy_weight`
--

LOCK TABLES `MSG_bm_policy_weight` WRITE;
/*!40000 ALTER TABLE `MSG_bm_policy_weight` DISABLE KEYS */;
INSERT INTO `MSG_bm_policy_weight` VALUES (2,'Thermodynamics','[0, 20, 0, 0, 0, 0, 0, 0]',2,11);
/*!40000 ALTER TABLE `MSG_bm_policy_weight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_bm_student_marks`
--

DROP TABLE IF EXISTS `MSG_bm_student_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_bm_student_marks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `marks` longtext,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  `roll_no` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MSG_bm__personid_id_2f7a68b45c916ffc_fk_TCH_personinformation_id` (`personid_id`),
  KEY `MSG_bm_s_sessionid_id_b44449b3cb4161a_fk_ADM_academic_session_id` (`sessionid_id`),
  CONSTRAINT `MSG_bm_s_sessionid_id_b44449b3cb4161a_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`),
  CONSTRAINT `MSG_bm__personid_id_2f7a68b45c916ffc_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_bm_student_marks`
--

LOCK TABLES `MSG_bm_student_marks` WRITE;
/*!40000 ALTER TABLE `MSG_bm_student_marks` DISABLE KEYS */;
INSERT INTO `MSG_bm_student_marks` VALUES (12,'Thermodynamics','[\'8\', \'7\', \'12\', \'11\', \'15\', \'18\', \'25\', \'40\']',2,11,'1105301'),(13,'Thermodynamics','[\'6\', \'6\', \'12\', \'0\', \'14\', \'19\', \'20\', \'35\']',2,11,'1105302'),(14,'Thermodynamics','[\'9\', \'8\', \'15\', \'10\', \'14\', \'16\', \'19\', \'40\']',2,11,'1105303'),(15,'Thermodynamics','[\'5\', \'4\', \'NA\', \'10\', \'11\', \'16\', \'13\', \'20\']',2,11,'1105304'),(16,'Thermodynamics','[\'4\', \'5\', \'NA\', \'NA\', \'9\', \'10\', \'14\', \'19\']',2,11,'1105305'),(17,'Thermodynamics','[\'8\', \'7\', \'10\', \'11\', \'9\', \'18\', \'24\', \'40\']',2,11,'1105306'),(18,'Thermodynamics','[\'5\', \'6\', \'13\', \'13\', \'11\', \'16\', \'22\', \'31\']',2,11,'1105307'),(19,'Thermodynamics','[\'7\', \'6\', \'11\', \'4\', \'10\', \'14\', \'20\', \'28\']',2,11,'1105308'),(20,'Thermodynamics','[\'6\', \'8\', \'12\', \'0\', \'NA\', \'19\', \'20\', \'15\']',2,11,'1105309'),(21,'Thermodynamics','[\'8\', \'9\', \'10\', \'13\', \'11\', \'18\', \'18\', \'34\']',2,11,'11053010');
/*!40000 ALTER TABLE `MSG_bm_student_marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_bm_weight`
--

DROP TABLE IF EXISTS `MSG_bm_weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_bm_weight` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bmoocs_weight` int(11) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MSG_bm__personid_id_7f1119b6ad238677_fk_TCH_personinformation_id` (`personid_id`),
  KEY `MSG_bm__sessionid_id_25ac48b4596e9401_fk_ADM_academic_session_id` (`sessionid_id`),
  CONSTRAINT `MSG_bm__personid_id_7f1119b6ad238677_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`),
  CONSTRAINT `MSG_bm__sessionid_id_25ac48b4596e9401_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_bm_weight`
--

LOCK TABLES `MSG_bm_weight` WRITE;
/*!40000 ALTER TABLE `MSG_bm_weight` DISABLE KEYS */;
INSERT INTO `MSG_bm_weight` VALUES (6,12,2,11,'Thermodynamics'),(7,10,2,11,'Data Structures and Algorithms');
/*!40000 ALTER TABLE `MSG_bm_weight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_content`
--

DROP TABLE IF EXISTS `MSG_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_content`
--

LOCK TABLES `MSG_content` WRITE;
/*!40000 ALTER TABLE `MSG_content` DISABLE KEYS */;
/*!40000 ALTER TABLE `MSG_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_coursegrade`
--

DROP TABLE IF EXISTS `MSG_coursegrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_coursegrade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gp_id` varchar(50) NOT NULL,
  `course_code` varchar(20) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MSG_cou_personid_id_4955c5ba8edda0ab_fk_TCH_personinformation_id` (`personid_id`),
  KEY `MSG_cou_sessionid_id_4b7f497a6e754d95_fk_ADM_academic_session_id` (`sessionid_id`),
  CONSTRAINT `MSG_cou_personid_id_4955c5ba8edda0ab_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`),
  CONSTRAINT `MSG_cou_sessionid_id_4b7f497a6e754d95_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_coursegrade`
--

LOCK TABLES `MSG_coursegrade` WRITE;
/*!40000 ALTER TABLE `MSG_coursegrade` DISABLE KEYS */;
INSERT INTO `MSG_coursegrade` VALUES (2,'2017-18/1/CS 101','CS 101',2,11),(3,'2017-18/1/ME 209','ME 209',2,11);
/*!40000 ALTER TABLE `MSG_coursegrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_grade_policy`
--

DROP TABLE IF EXISTS `MSG_grade_policy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_grade_policy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gp_id` varchar(50) NOT NULL,
  `abbreviation` varchar(4) NOT NULL,
  `assignment` varchar(20) NOT NULL,
  `total` int(11) NOT NULL,
  `mandatory` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_grade_policy`
--

LOCK TABLES `MSG_grade_policy` WRITE;
/*!40000 ALTER TABLE `MSG_grade_policy` DISABLE KEYS */;
INSERT INTO `MSG_grade_policy` VALUES (10,'2017-18/1/CS 101','QZ','quiz',7,6,100),(11,'2017-18/1/ME 209','QZ','quiz',5,4,40),(12,'2017-18/1/ME 209','MS','mid_sem',1,1,30),(13,'2017-18/1/ME 209','ES','end_sem',1,1,30);
/*!40000 ALTER TABLE `MSG_grade_policy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MSG_student_marks`
--

DROP TABLE IF EXISTS `MSG_student_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MSG_student_marks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roll_no` varchar(30) NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MSG_student_marks`
--

LOCK TABLES `MSG_student_marks` WRITE;
/*!40000 ALTER TABLE `MSG_student_marks` DISABLE KEYS */;
INSERT INTO `MSG_student_marks` VALUES (1,'1105301',78),(2,'1105302',65),(3,'1105303',88),(4,'1105304',69),(5,'1105305',55),(6,'1105306',85),(7,'1105307',70),(8,'1105308',90),(9,'1105309',45),(10,'11053010',25);
/*!40000 ALTER TABLE `MSG_student_marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TCH_courseallotment`
--

DROP TABLE IF EXISTS `TCH_courseallotment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TCH_courseallotment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseid_id` int(11) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `sessionid_id` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TCH_courseallo_courseid_id_6efa223118fc389c_fk_ADM_all_course_id` (`courseid_id`),
  KEY `TCH_courseallotment_92564f6d` (`personid_id`),
  KEY `TCH_courseallotment_fab9fb3f` (`sessionid_id`),
  CONSTRAINT `TCH_courseallo_courseid_id_6efa223118fc389c_fk_ADM_all_course_id` FOREIGN KEY (`courseid_id`) REFERENCES `ADM_all_course` (`id`),
  CONSTRAINT `TCH_cou_personid_id_28960db32987b43c_fk_TCH_personinformation_id` FOREIGN KEY (`personid_id`) REFERENCES `TCH_personinformation` (`id`),
  CONSTRAINT `TCH_cou_sessionid_id_3b1bf2ab2ac3b0ae_fk_ADM_academic_session_id` FOREIGN KEY (`sessionid_id`) REFERENCES `ADM_academic_session` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TCH_courseallotment`
--

LOCK TABLES `TCH_courseallotment` WRITE;
/*!40000 ALTER TABLE `TCH_courseallotment` DISABLE KEYS */;
INSERT INTO `TCH_courseallotment` VALUES (1,10,1,11,1),(24,11,4,11,1),(27,16,2,11,1),(28,11,2,11,1),(29,16,6,11,1),(30,20,2,11,1),(31,11,1,11,1);
/*!40000 ALTER TABLE `TCH_courseallotment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TCH_evaluation_marks`
--

DROP TABLE IF EXISTS `TCH_evaluation_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TCH_evaluation_marks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roll_no` varchar(50) NOT NULL,
  `marks` double NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `evalid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TCH_evaluation_marks_c68bcf75` (`evalid_id`),
  CONSTRAINT `TCH_evalua_evalid_id_2597606e0c92312c_fk_TCH_evaluation_table_id` FOREIGN KEY (`evalid_id`) REFERENCES `TCH_evaluation_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TCH_evaluation_marks`
--

LOCK TABLES `TCH_evaluation_marks` WRITE;
/*!40000 ALTER TABLE `TCH_evaluation_marks` DISABLE KEYS */;
INSERT INTO `TCH_evaluation_marks` VALUES (1,'101',14,1,1),(2,'102',8,1,1),(3,'103',10,1,1),(4,'104',12,1,1),(5,'105',9,1,1),(6,'106',8,1,1),(7,'107',13,1,1),(8,'108',12,1,1),(9,'109',12,1,1),(10,'110',10,1,1),(11,'101',12,1,3),(12,'102',6,1,3),(13,'103',5,1,3),(14,'104',13,1,3),(15,'105',6,1,3),(16,'106',10,1,3),(17,'107',11,1,3),(18,'108',9,1,3),(19,'109',15,1,3),(20,'110',13,1,3),(21,'101',6,1,4),(22,'102',9,1,4),(23,'103',8,1,4),(24,'104',10,1,4),(25,'105',11,1,4),(26,'106',12,1,4),(27,'107',6,1,4),(28,'108',9,1,4),(29,'109',13,1,4),(30,'110',15,1,4),(31,'101',15,1,5),(32,'102',10,1,5),(33,'103',12,1,5),(34,'104',5,1,5),(35,'105',3,1,5),(36,'106',11,1,5),(37,'107',10,1,5),(38,'108',4,1,5),(39,'109',2,1,5),(40,'110',6,1,5),(41,'101',13,1,6),(42,'102',3,1,6),(43,'103',4,1,6),(44,'104',15,1,6),(45,'105',14,1,6),(46,'106',6,1,6),(47,'107',1,1,6),(48,'108',15,1,6),(49,'109',7,1,6),(50,'110',9,1,6),(51,'101',40,1,7),(52,'102',35,1,7),(53,'103',36,1,7),(54,'104',19,1,7),(55,'105',35,1,7),(56,'106',32,1,7),(57,'107',26,1,7),(58,'108',49,1,7),(59,'109',46,1,7),(60,'110',41,1,7),(61,'101',26,1,8),(62,'102',18,1,8),(63,'103',16,1,8),(64,'104',19,1,8),(65,'105',29,1,8),(66,'106',28,1,8),(67,'107',23,1,8),(68,'108',24,1,8),(69,'109',27,1,8),(70,'110',28,1,8);
/*!40000 ALTER TABLE `TCH_evaluation_marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TCH_evaluation_table`
--

DROP TABLE IF EXISTS `TCH_evaluation_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TCH_evaluation_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eval_name` varchar(30) NOT NULL,
  `eval_no` varchar(30) DEFAULT NULL,
  `max_marks` double NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `courseallotid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TCH__courseallotid_id_45ec60ea5f2bf29e_fk_TCH_courseallotment_id` (`courseallotid_id`),
  CONSTRAINT `TCH__courseallotid_id_45ec60ea5f2bf29e_fk_TCH_courseallotment_id` FOREIGN KEY (`courseallotid_id`) REFERENCES `TCH_courseallotment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TCH_evaluation_table`
--

LOCK TABLES `TCH_evaluation_table` WRITE;
/*!40000 ALTER TABLE `TCH_evaluation_table` DISABLE KEYS */;
INSERT INTO `TCH_evaluation_table` VALUES (1,'quiz','1',15,1,30),(3,'quiz','2',15,1,30),(4,'quiz','3',20,1,30),(5,'quiz','4',20,1,30),(6,'quiz','5',15,1,30),(7,'mid_sem','1',50,1,30),(8,'end_sem','1',30,1,30);
/*!40000 ALTER TABLE `TCH_evaluation_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TCH_personinformation`
--

DROP TABLE IF EXISTS `TCH_personinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TCH_personinformation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `titleid` int(11) DEFAULT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `designation` int(11) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `experience` varchar(45) DEFAULT NULL,
  `qualification` varchar(45) DEFAULT NULL,
  `telephone1` varchar(12) NOT NULL,
  `telephone2` varchar(12) DEFAULT NULL,
  `createdondate` date NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `departmentid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TCH_personinformation_bf5e6aee` (`departmentid_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TCH_personinformation`
--

LOCK TABLES `TCH_personinformation` WRITE;
/*!40000 ALTER TABLE `TCH_personinformation` DISABLE KEYS */;
INSERT INTO `TCH_personinformation` VALUES (1,'rajeev@gmail.com',0,'rajeev','kumar',5,'MALE','0','0','0','0','2015-09-25',1,3),(2,'rahul@gmail.com',0,'rahul','parashar',5,'MALE','0','0','0','0','2015-09-25',1,3),(3,'admin@gmail.com',0,'admin','admin',0,'MALE','0','0','0','0','2015-09-25',1,0),(4,'ramesh@gmail.com',0,'ramesh','gaikwad',5,'MALE','0','0','0','0','2015-09-29',1,6),(5,'sandip@gmail.com',0,'sandip','kumar',5,'MALE','0','0','0','0','2015-10-07',1,8),(6,'sunny@gmail.com',0,'sunny','rathod',5,'MALE','0','0','0','0','2015-10-07',1,6);
/*!40000 ALTER TABLE `TCH_personinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add all_deprtment',7,'add_all_deprtment'),(20,'Can change all_deprtment',7,'change_all_deprtment'),(21,'Can delete all_deprtment',7,'delete_all_deprtment'),(22,'Can add userlogin',8,'add_userlogin'),(23,'Can change userlogin',8,'change_userlogin'),(24,'Can delete userlogin',8,'delete_userlogin'),(25,'Can add all_course',9,'add_all_course'),(26,'Can change all_course',9,'change_all_course'),(27,'Can delete all_course',9,'delete_all_course'),(28,'Can add personinformation',10,'add_personinformation'),(29,'Can change personinformation',10,'change_personinformation'),(30,'Can delete personinformation',10,'delete_personinformation'),(31,'Can add courseallotment',11,'add_courseallotment'),(32,'Can change courseallotment',11,'change_courseallotment'),(33,'Can delete courseallotment',11,'delete_courseallotment'),(34,'Can add academic_session',12,'add_academic_session'),(35,'Can change academic_session',12,'change_academic_session'),(36,'Can delete academic_session',12,'delete_academic_session'),(37,'Can add grade_policy',13,'add_grade_policy'),(38,'Can change grade_policy',13,'change_grade_policy'),(39,'Can delete grade_policy',13,'delete_grade_policy'),(43,'Can add content',15,'add_content'),(44,'Can change content',15,'change_content'),(45,'Can delete content',15,'delete_content'),(58,'Can add course grade',20,'add_coursegrade'),(59,'Can change course grade',20,'change_coursegrade'),(60,'Can delete course grade',20,'delete_coursegrade'),(61,'Can add bm_weight',21,'add_bm_weight'),(62,'Can change bm_weight',21,'change_bm_weight'),(63,'Can delete bm_weight',21,'delete_bm_weight'),(64,'Can add bm_grade_policy',22,'add_bm_grade_policy'),(65,'Can change bm_grade_policy',22,'change_bm_grade_policy'),(66,'Can delete bm_grade_policy',22,'delete_bm_grade_policy'),(67,'Can add b m_policy_weight',23,'add_bm_policy_weight'),(68,'Can change b m_policy_weight',23,'change_bm_policy_weight'),(69,'Can delete b m_policy_weight',23,'delete_bm_policy_weight'),(70,'Can add student_marks',24,'add_student_marks'),(71,'Can change student_marks',24,'change_student_marks'),(72,'Can delete student_marks',24,'delete_student_marks'),(73,'Can add bm_max_marks',25,'add_bm_max_marks'),(74,'Can change bm_max_marks',25,'change_bm_max_marks'),(75,'Can delete bm_max_marks',25,'delete_bm_max_marks'),(76,'Can add bm_student_marks',26,'add_bm_student_marks'),(77,'Can change bm_student_marks',26,'change_bm_student_marks'),(78,'Can delete bm_student_marks',26,'delete_bm_student_marks'),(79,'Can add teacher_mapping',27,'add_teacher_mapping'),(80,'Can change teacher_mapping',27,'change_teacher_mapping'),(81,'Can delete teacher_mapping',27,'delete_teacher_mapping'),(82,'Can add student_mapping',28,'add_student_mapping'),(83,'Can change student_mapping',28,'change_student_mapping'),(84,'Can delete student_mapping',28,'delete_student_mapping'),(85,'Can add moodle',29,'add_moodle'),(86,'Can change moodle',29,'change_moodle'),(87,'Can delete moodle',29,'delete_moodle'),(88,'Can add evaluation_table',30,'add_evaluation_table'),(89,'Can change evaluation_table',30,'change_evaluation_table'),(90,'Can delete evaluation_table',30,'delete_evaluation_table'),(91,'Can add evaluation_marks',31,'add_evaluation_marks'),(92,'Can change evaluation_marks',31,'change_evaluation_marks'),(93,'Can delete evaluation_marks',31,'delete_evaluation_marks'),(94,'Can add course_mapping',32,'add_course_mapping'),(95,'Can change course_mapping',32,'change_course_mapping'),(96,'Can delete course_mapping',32,'delete_course_mapping');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$4yCS52Uzt06N$TYvhqgvlP7gVRpD5fULRhZKAls7VQ9qH5K6rDBYpsuM=','2016-05-19 19:00:14',1,'root','','','root@gmail.com',1,1,'2015-09-23 10:29:26'),(4,'pbkdf2_sha256$20000$30sZMzffQmqu$DQiT/JzHz92Ty6kN6tZiU+r6UJzDC1nXF24KT2HvaJE=','2016-05-19 18:55:22',0,'admin@gmail.com','saket ','kumar','admin@gmail.com',0,1,'2015-09-24 12:52:26'),(5,'pbkdf2_sha256$20000$JABhSmmJmFZ4$ushRrGTesBYbmmzmKWk1lPjY/WfiFtl1+uyGsUsCbqU=','2015-10-05 09:19:21',0,'rajeev@gmail.com','rajeev','kumar','rajeev@gmail.com',0,1,'2015-09-24 12:58:22'),(6,'pbkdf2_sha256$20000$eioQb9PS4OJ5$HaRG3Z4DeOaIM6ZOacGQAFbOpigbvgtLulz1IvC/UZQ=','2016-05-12 08:35:44',0,'rahul@gmail.com','rahul','parashar','rahul@gmail.com',0,1,'2015-09-26 15:30:26');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,4,1),(2,4,2),(3,4,3),(4,4,4),(5,4,5),(6,4,6),(7,4,7),(8,4,8),(9,4,9),(10,4,10),(11,4,11),(12,4,12),(13,4,13),(14,4,14),(15,4,15),(16,4,16),(17,4,17),(18,4,18),(19,4,19),(20,4,20),(21,4,21),(22,4,22),(23,4,23),(24,4,24),(25,4,25),(26,4,26),(27,4,27);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-09-23 12:50:10','2','admin@workshop.com',1,'',4,1),(2,'2015-09-23 12:50:57','3','a@workshop.com',1,'',4,1),(3,'2015-09-23 12:52:17','1','Userlogin object',1,'',8,1),(4,'2015-09-23 12:54:24','1','Userlogin object',2,'No fields changed.',8,1),(5,'2015-09-24 12:47:08','1','Userlogin object',3,'',8,1),(6,'2015-09-24 12:51:12','3','a@workshop.com',3,'',4,1),(7,'2015-09-24 12:51:12','2','admin@workshop.com',3,'',4,1),(8,'2015-09-24 12:52:27','4','admin@gmailcom',1,'',4,1),(9,'2015-09-24 12:57:32','4','admin@gmail.com',2,'Changed username, first_name, last_name, email and user_permissions.',4,1),(10,'2015-09-24 12:58:22','5','rajeev@gmail.com',1,'',4,1),(11,'2015-09-24 13:00:16','5','rajeev@gmail.com',2,'Changed first_name, last_name and email.',4,1),(12,'2015-09-24 13:01:19','5','rajeev@gmail.com',2,'No fields changed.',4,1),(13,'2015-09-24 13:01:39','5','rajeev@gmail.com',2,'No fields changed.',4,1),(14,'2015-09-24 13:03:26','2','Userlogin object',1,'',8,1),(15,'2015-09-24 13:03:39','2','Userlogin object',2,'Changed last_login.',8,1),(16,'2015-09-24 13:05:58','3','Userlogin object',1,'',8,1),(17,'2015-09-24 13:06:11','2','Userlogin object',2,'Changed nooflogins.',8,1),(18,'2015-09-25 10:43:17','2','Userlogin object',2,'No fields changed.',8,1),(19,'2015-09-25 10:44:37','4','admin@gmail.com',2,'Changed password.',4,1),(20,'2015-09-25 14:44:31','1','Personinformation object',1,'',10,1),(21,'2015-09-25 14:44:41','1','Personinformation object',2,'No fields changed.',10,1),(22,'2015-09-25 14:45:40','2','Personinformation object',1,'',10,1),(23,'2015-09-25 14:45:49','1','Personinformation object',2,'No fields changed.',10,1),(24,'2015-09-25 14:48:43','1','Courseallotment object',1,'',11,1),(25,'2015-09-25 14:49:16','2','Courseallotment object',1,'',11,1),(26,'2015-09-25 14:50:32','3','Courseallotment object',1,'',11,1),(27,'2015-09-25 15:27:41','3','Personinformation object',1,'',10,1),(28,'2015-09-26 15:23:56','3','Courseallotment object',2,'Changed sessionid.',11,1),(29,'2015-09-26 15:24:02','2','Courseallotment object',2,'Changed sessionid.',11,1),(30,'2015-09-26 15:24:08','1','Courseallotment object',2,'Changed sessionid.',11,1),(31,'2015-09-26 15:24:38','4','Courseallotment object',1,'',11,1),(32,'2015-09-26 15:25:06','5','Courseallotment object',1,'',11,1),(33,'2015-09-26 15:25:20','2','Courseallotment object',2,'Changed courseid.',11,1),(34,'2015-09-26 15:30:26','6','rahul@gmail.com',1,'',4,1),(35,'2015-09-26 15:32:49','6','rahul@gmail.com',2,'Changed first_name, last_name, email and last_login.',4,1),(36,'2015-09-26 15:41:18','4','Userlogin object',1,'',8,1),(37,'2015-09-26 16:44:35','6','Courseallotment object',1,'',11,1),(38,'2015-09-26 16:44:47','7','Courseallotment object',1,'',11,1),(39,'2015-09-29 13:39:26','2','Personinformation object',2,'Changed departmentid.',10,1),(40,'2015-09-29 13:39:37','1','Personinformation object',2,'Changed departmentid.',10,1),(41,'2015-09-29 13:41:18','4','Personinformation object',1,'',10,1),(42,'2015-09-29 13:41:23','1','Personinformation object',2,'No fields changed.',10,1),(43,'2015-10-01 13:59:04','18','All_course object',2,'Changed course_code.',9,1),(44,'2015-10-01 13:59:35','12','All_course object',2,'Changed course_code.',9,1),(45,'2015-10-06 05:13:52','3','Grade_policy object',2,'Changed assignment.',13,1),(46,'2015-10-06 05:36:10','9','Grade_policy object',3,'',13,1),(47,'2015-10-06 05:36:10','8','Grade_policy object',3,'',13,1),(48,'2015-10-06 05:36:10','7','Grade_policy object',3,'',13,1),(49,'2015-10-06 05:36:10','6','Grade_policy object',3,'',13,1),(50,'2015-10-06 05:36:10','5','Grade_policy object',3,'',13,1),(51,'2015-10-06 05:36:10','4','Grade_policy object',3,'',13,1),(52,'2015-10-06 05:36:10','3','Grade_policy object',3,'',13,1),(53,'2015-10-06 05:36:10','2','Grade_policy object',3,'',13,1),(54,'2015-10-06 05:36:35','1','CourseGrade object',3,'',20,1),(55,'2015-10-06 07:33:40','9','All_deprtment object',3,'',7,1),(56,'2015-10-06 07:34:24','5','All_deprtment object',3,'',7,1),(57,'2015-10-06 07:35:18','10','All_deprtment object',1,'',7,1),(58,'2015-10-07 03:29:03','5','Personinformation object',1,'',10,1),(59,'2015-10-07 03:30:19','6','Personinformation object',1,'',10,1),(60,'2015-10-07 03:31:29','4','Personinformation object',2,'Changed departmentid.',10,1),(61,'2015-10-07 15:03:50','1','Student_marks object',1,'',24,1),(62,'2015-10-07 15:03:59','2','Student_marks object',1,'',24,1),(63,'2015-10-07 15:04:07','3','Student_marks object',1,'',24,1),(64,'2015-10-07 15:04:19','4','Student_marks object',1,'',24,1),(65,'2015-10-07 15:04:27','5','Student_marks object',1,'',24,1),(66,'2015-10-07 15:04:36','6','Student_marks object',1,'',24,1),(67,'2015-10-07 15:04:46','7','Student_marks object',1,'',24,1),(68,'2015-10-07 15:04:59','8','Student_marks object',1,'',24,1),(69,'2015-10-07 15:05:07','9','Student_marks object',1,'',24,1),(70,'2015-10-07 15:05:26','10','Student_marks object',1,'',24,1),(71,'2015-10-09 05:30:57','10','Academic_session object',2,'Changed year.',12,1),(72,'2015-10-09 05:31:08','11','Academic_session object',2,'Changed year.',12,1),(73,'2015-10-09 05:31:12','11','Academic_session object',2,'No fields changed.',12,1),(74,'2015-10-09 07:00:52','5','Bm_weight object',3,'',21,1),(75,'2015-10-09 07:00:58','4','Bm_weight object',3,'',21,1),(76,'2015-10-09 07:01:08','3','Bm_weight object',3,'',21,1),(77,'2015-10-09 07:05:51','2','Bm_weight object',3,'',21,1),(78,'2015-10-09 07:45:51','1','Bm_policy_weight object',3,'',23,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'ADM','academic_session'),(9,'ADM','all_course'),(7,'ADM','all_deprtment'),(32,'ADM','course_mapping'),(29,'ADM','moodle'),(28,'ADM','student_mapping'),(27,'ADM','teacher_mapping'),(8,'ADM','userlogin'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(22,'MSG','bm_grade_policy'),(25,'MSG','bm_max_marks'),(23,'MSG','bm_policy_weight'),(26,'MSG','bm_student_marks'),(21,'MSG','bm_weight'),(15,'MSG','content'),(20,'MSG','coursegrade'),(13,'MSG','grade_policy'),(24,'MSG','student_marks'),(6,'sessions','session'),(11,'TCH','courseallotment'),(31,'TCH','evaluation_marks'),(30,'TCH','evaluation_table'),(10,'TCH','personinformation');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-09-22 13:10:34'),(2,'auth','0001_initial','2015-09-22 13:10:36'),(3,'admin','0001_initial','2015-09-22 13:10:37'),(4,'contenttypes','0002_remove_content_type_name','2015-09-22 13:10:37'),(5,'auth','0002_alter_permission_name_max_length','2015-09-22 13:10:37'),(6,'auth','0003_alter_user_email_max_length','2015-09-22 13:10:38'),(7,'auth','0004_alter_user_username_opts','2015-09-22 13:10:38'),(8,'auth','0005_alter_user_last_login_null','2015-09-22 13:10:38'),(9,'auth','0006_require_contenttypes_0002','2015-09-22 13:10:38'),(10,'sessions','0001_initial','2015-09-22 13:10:38'),(11,'ADM','0001_initial','2015-09-23 05:04:10'),(12,'ADM','0002_userlogin','2015-09-23 12:45:15'),(13,'ADM','0003_all_course','2015-09-24 10:55:46'),(14,'ADM','0004_auto_20150924_1833','2015-09-24 18:42:32'),(15,'ADM','0005_auto_20150924_1842','2015-09-24 18:42:56'),(16,'ADM','0006_auto_20150924_1847','2015-09-24 18:48:17'),(17,'ADM','0007_auto_20150924_1920','2015-09-24 19:20:20'),(18,'TCH','0001_initial','2015-09-25 14:37:23'),(19,'ADM','0008_academic_session','2015-09-26 12:25:22'),(20,'TCH','0002_auto_20150926_1225','2015-09-26 12:25:22'),(21,'ADM','0009_auto_20150926_1326','2015-09-26 13:26:28'),(22,'ADM','0010_auto_20150926_1332','2015-09-26 13:32:53'),(23,'TCH','0003_auto_20150926_1520','2015-09-26 15:23:17'),(24,'MSG','0001_initial','2015-09-27 09:08:34'),(25,'MSG','0002_grade_policy_master','2015-09-27 09:08:35'),(26,'MSG','0003_auto_20150913_1323','2015-09-27 09:08:35'),(27,'MSG','0004_auto_20150913_1331','2015-09-27 09:08:36'),(28,'MSG','0005_coursegrade_errorcontent_grade_policy','2015-09-27 09:08:37'),(29,'MSG','0006_auto_20150913_1338','2015-09-27 09:08:37'),(30,'MSG','0007_auto_20150913_1439','2015-09-27 09:08:37'),(31,'MSG','0008_auto_20150913_1527','2015-09-27 09:08:37'),(32,'MSG','0009_coursegrade_errorcontent_grade_policy','2015-09-27 09:08:38'),(33,'MSG','0010_auto_20150915_0510','2015-09-27 09:08:39'),(34,'MSG','0011_auto_20150915_0534','2015-09-27 09:08:39'),(35,'MSG','0012_auto_20150915_0535','2015-09-27 09:08:39'),(36,'MSG','0013_uploadfile','2015-09-27 09:08:39'),(37,'MSG','0014_auto_20150916_1024','2015-09-27 09:08:40'),(38,'MSG','0015_delete_uploadedfiles','2015-09-27 09:08:40'),(39,'MSG','0016_content','2015-09-27 09:08:40'),(40,'MSG','0017_auto_20150917_0707','2015-09-27 09:08:40'),(41,'MSG','0018_auto_20150917_0722','2015-09-27 09:08:41'),(42,'MSG','0019_max_marks_student_marks','2015-09-27 09:08:41'),(43,'MSG','0020_student_marks_gp_id','2015-09-27 09:08:41'),(44,'MSG','0021_remove_student_marks_gp_id','2015-09-27 09:08:42'),(45,'MSG','0022_bm_weight','2015-09-27 09:08:42'),(46,'MSG','0023_delete_bm_weight','2015-09-27 09:08:42'),(47,'MSG','0024_bm_weight','2015-09-27 09:08:42'),(48,'MSG','0025_auto_20150919_0749','2015-09-27 09:08:43'),(49,'MSG','0026_auto_20150920_1403','2015-09-27 09:08:43'),(50,'MSG','0027_auto_20150927_0910','2015-09-27 09:10:14'),(51,'TCH','0004_courseallotment_is_active','2015-09-28 09:19:12'),(52,'MSG','0028_content_grade_policy','2015-09-28 09:19:13'),(53,'MSG','0029_auto_20150929_0833','2015-09-29 08:33:35'),(54,'MSG','0030_bm_weight','2015-09-29 10:02:09'),(55,'TCH','0005_auto_20150929_1338','2015-09-29 14:13:42'),(56,'MSG','0031_bm_weight_course_name','2015-09-30 14:19:01'),(57,'MSG','0032_bm_grade_policy','2015-10-07 11:25:40'),(58,'MSG','0033_bm_policy_weight','2015-10-07 14:04:13'),(59,'MSG','0034_student_marks','2015-10-07 15:01:56'),(60,'MSG','0035_bm_max_marks_bm_student_marks','2015-10-07 15:58:20'),(61,'MSG','0036_bm_student_marks_roll_no','2015-10-07 16:38:59'),(62,'MSG','0037_auto_20151007_1842','2015-10-07 18:42:42'),(63,'ADM','0011_teacher_mapping','2016-04-14 06:59:27'),(64,'ADM','0012_student_mapping','2016-04-15 01:11:14'),(65,'ADM','0013_moodle','2016-04-18 10:30:08'),(66,'TCH','0006_auto_20160422_0907','2016-04-22 09:20:22'),(67,'TCH','0007_auto_20160422_0921','2016-04-22 09:21:41'),(68,'ADM','0014_course_mapping','2016-05-05 06:14:49');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0fryb5tw1hx7kht6dj3wtda556r2wn6e','YjdjZTI1OTE0MDMwYzQ1MGMxZWFiODY4ZTMwNjY4YjhiMTMzNWRjOTp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsInJvbGVuYW1lIjoiVGVhY2hlciIsIl9hdXRoX3VzZXJfaGFzaCI6IjY2NGEyMjUzNDM3NjczZjFlMTg1NWI3MmYwOGM1NGE4NDBjYjZmMjIifQ==','2016-05-26 08:35:44'),('30j9hzr4vwhtjs2yvrsxr2z63dath64p','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-10 15:33:48'),('3xcyl1fiqull7dcd8qt21fo3pw6rgijf','YjdjZTI1OTE0MDMwYzQ1MGMxZWFiODY4ZTMwNjY4YjhiMTMzNWRjOTp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsInJvbGVuYW1lIjoiVGVhY2hlciIsIl9hdXRoX3VzZXJfaGFzaCI6IjY2NGEyMjUzNDM3NjczZjFlMTg1NWI3MmYwOGM1NGE4NDBjYjZmMjIifQ==','2016-03-24 07:04:47'),('7ba0fpzi7a97keqhm98taqd4zicobbmt','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-07 13:57:31'),('8owjnjq7qmqzf71xm7vvd74t799vm6j0','YTA4ZWM3YjMyOTE4MDU1NmRmNTEzZTg5ZjEzZWEwNTFmNzc2ZDE1Yzp7ImVtYWlsX2lkIjoicmFodWxAZ21haWwuY29tIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjY0YTIyNTM0Mzc2NzNmMWUxODU1YjcyZjA4YzU0YTg0MGNiNmYyMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjYiLCJuYW1lIjoicmFodWwifQ==','2015-10-18 07:15:57'),('an1c52m0pyohljdq4z3f9z3j2k9bvizl','MGFhMDcyYTk3NzcxNmQzNTk3NmUzNDJjZDRmMzQwMjNkNzNlYzAzODp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImNuYW1lIjoiVGhlcm1vZHluYW1pY3MiLCJyb2xlbmFtZSI6IlRlYWNoZXIiLCJfYXV0aF91c2VyX2hhc2giOiI2NjRhMjI1MzQzNzY3M2YxZTE4NTViNzJmMDhjNTRhODQwY2I2ZjIyIn0=','2015-10-22 12:15:37'),('av4k2fdb5wbmf3xgn065rbc8958zcvpx','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-08 07:44:20'),('c66dxxr98f6suesxy0a52yqm72dvbeqq','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-08 11:47:01'),('d6jyjw3kzixpjb865jsrrazj2lhp71tp','ODc5ZmIxOGQ4OWQ4MGZlN2NlNmNhMDk0ZTZhYjk5ZThiNmIyMjEzMjp7Im5hbWUiOiJzYWtldCAiLCJfYXV0aF91c2VyX2lkIjoiNCIsImVtYWlsX2lkIjoiYWRtaW5AZ21haWwuY29tIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJyb2xlbmFtZSI6IkFkbWluIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWRmYWNiYjkyNmNlMjhlYTI2ZWYwNWJhZDUxMjAxODNiNjQ4OTE0MyJ9','2016-05-29 07:00:59'),('dameiay9j4p3591cf0vzfr1bq81p1dzy','MGFhMDcyYTk3NzcxNmQzNTk3NmUzNDJjZDRmMzQwMjNkNzNlYzAzODp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImNuYW1lIjoiVGhlcm1vZHluYW1pY3MiLCJyb2xlbmFtZSI6IlRlYWNoZXIiLCJfYXV0aF91c2VyX2hhc2giOiI2NjRhMjI1MzQzNzY3M2YxZTE4NTViNzJmMDhjNTRhODQwY2I2ZjIyIn0=','2015-10-30 19:35:00'),('djigm6azaxhbnsw0d52g59gtpa7z1j03','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-08 11:34:56'),('geeowglh65vg7i41sb766fe666bfqej1','NTIyMTBjY2YzYjQyNTI1YjM1MmU5Y2U4OTI0Yzc2MjA1OWYzMmFlZDp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNmMxZWIxNmMzM2Q3MmJlYWFmMDE2YTI5N2I0ZjMwNDVmN2I4OWNjZCJ9','2016-06-03 07:45:15'),('gjfyjnv64oenjmzbqikbh3mclzw1crd0','YTA4ZWM3YjMyOTE4MDU1NmRmNTEzZTg5ZjEzZWEwNTFmNzc2ZDE1Yzp7ImVtYWlsX2lkIjoicmFodWxAZ21haWwuY29tIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjY0YTIyNTM0Mzc2NzNmMWUxODU1YjcyZjA4YzU0YTg0MGNiNmYyMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjYiLCJuYW1lIjoicmFodWwifQ==','2015-10-18 13:51:24'),('i980jwwfx3nmqfd7ifnulojgoovczvbk','YjdjZTI1OTE0MDMwYzQ1MGMxZWFiODY4ZTMwNjY4YjhiMTMzNWRjOTp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsInJvbGVuYW1lIjoiVGVhY2hlciIsIl9hdXRoX3VzZXJfaGFzaCI6IjY2NGEyMjUzNDM3NjczZjFlMTg1NWI3MmYwOGM1NGE4NDBjYjZmMjIifQ==','2015-10-20 06:37:53'),('ii8uwxnh1zhilg0bilp1i7lcsv0rj0yp','M2RjMmY5NjdkMWIzMTdjYTllOTQ3ZGM1N2U2YWUxZDVmMTIxZDQyOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGZhY2JiOTI2Y2UyOGVhMjZlZjA1YmFkNTEyMDE4M2I2NDg5MTQzIn0=','2016-05-12 11:05:33'),('kfs5oo23ajtr4cxq0o0gaolegxhbuuwu','YjdjZTI1OTE0MDMwYzQ1MGMxZWFiODY4ZTMwNjY4YjhiMTMzNWRjOTp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsInJvbGVuYW1lIjoiVGVhY2hlciIsIl9hdXRoX3VzZXJfaGFzaCI6IjY2NGEyMjUzNDM3NjczZjFlMTg1NWI3MmYwOGM1NGE4NDBjYjZmMjIifQ==','2016-05-14 23:23:30'),('kqwfz4jgr6ptahu2gqt52sld0061hhqp','YjdjZTI1OTE0MDMwYzQ1MGMxZWFiODY4ZTMwNjY4YjhiMTMzNWRjOTp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsInJvbGVuYW1lIjoiVGVhY2hlciIsIl9hdXRoX3VzZXJfaGFzaCI6IjY2NGEyMjUzNDM3NjczZjFlMTg1NWI3MmYwOGM1NGE4NDBjYjZmMjIifQ==','2015-10-20 10:51:55'),('kr1z60cofrz0979dfcx6cnbdw9u9q2yf','YjdjZTI1OTE0MDMwYzQ1MGMxZWFiODY4ZTMwNjY4YjhiMTMzNWRjOTp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsInJvbGVuYW1lIjoiVGVhY2hlciIsIl9hdXRoX3VzZXJfaGFzaCI6IjY2NGEyMjUzNDM3NjczZjFlMTg1NWI3MmYwOGM1NGE4NDBjYjZmMjIifQ==','2016-02-11 10:24:03'),('ksxllu2vuonutl52kbn5amqo9wcalfvh','NjhhMWQ5MTAwMDBjOWNkMDRhZjQwNTgwOGQ5YTllNjAwYzEyYzI5MTp7ImVtYWlsX2lkIjoiYWRtaW5AZ21haWwuY29tIiwiX2F1dGhfdXNlcl9oYXNoIjoiODkyNTFlNzZmOTlmOGZmYmM2MGQ5NWQ5NThmYTk4OGJhMWU0Y2M5NyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJuYW1lIjoic2FrZXQgIn0=','2015-10-14 11:40:16'),('lzkt0nefx17r3dx0epfvpreny6c2tnsi','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-07 13:55:45'),('oreco339br730qz76d3s5g15orxu384v','M2Q1MzQ0YTg3YzlkZjM1NmUxNTAwMGJjZGUxZjc0NzgyMTFkMzUxZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImFkZmFjYmI5MjZjZTI4ZWEyNmVmMDViYWQ1MTIwMTgzYjY0ODkxNDMiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-10-15 14:43:24'),('r99pqcxp8clbxam9yjh26smw4ay3qzu8','YTA4ZWM3YjMyOTE4MDU1NmRmNTEzZTg5ZjEzZWEwNTFmNzc2ZDE1Yzp7ImVtYWlsX2lkIjoicmFodWxAZ21haWwuY29tIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjY0YTIyNTM0Mzc2NzNmMWUxODU1YjcyZjA4YzU0YTg0MGNiNmYyMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjYiLCJuYW1lIjoicmFodWwifQ==','2015-10-13 06:06:12'),('s114a7o0svayoh3jwpqe18aw1bljqkx7','M2RjMmY5NjdkMWIzMTdjYTllOTQ3ZGM1N2U2YWUxZDVmMTIxZDQyOTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZGZhY2JiOTI2Y2UyOGVhMjZlZjA1YmFkNTEyMDE4M2I2NDg5MTQzIn0=','2015-10-23 05:03:20'),('smlh5yw3ttzs0ezakevnux68pffeqm5a','N2M2N2Q4MGQ2ZmY5MTJmOTJiNzY2OTAxY2MzZGJmZWFhOWQ2YzQ4Yzp7fQ==','2015-10-08 11:40:59'),('t1ot6vdpwhydtjiztdxl9no5tj77i95n','ODc5ZmIxOGQ4OWQ4MGZlN2NlNmNhMDk0ZTZhYjk5ZThiNmIyMjEzMjp7Im5hbWUiOiJzYWtldCAiLCJfYXV0aF91c2VyX2lkIjoiNCIsImVtYWlsX2lkIjoiYWRtaW5AZ21haWwuY29tIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJyb2xlbmFtZSI6IkFkbWluIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWRmYWNiYjkyNmNlMjhlYTI2ZWYwNWJhZDUxMjAxODNiNjQ4OTE0MyJ9','2015-11-04 05:24:44'),('vkltvopb8azldthzkr0musu0ysfo08ns','MGFhMDcyYTk3NzcxNmQzNTk3NmUzNDJjZDRmMzQwMjNkNzNlYzAzODp7Im5hbWUiOiJyYWh1bCIsIl9hdXRoX3VzZXJfaWQiOiI2IiwiZW1haWxfaWQiOiJyYWh1bEBnbWFpbC5jb20iLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImNuYW1lIjoiVGhlcm1vZHluYW1pY3MiLCJyb2xlbmFtZSI6IlRlYWNoZXIiLCJfYXV0aF91c2VyX2hhc2giOiI2NjRhMjI1MzQzNzY3M2YxZTE4NTViNzJmMDhjNTRhODQwY2I2ZjIyIn0=','2015-10-28 06:54:58'),('za1okxe4ah0e9oe8fqugtouvsscghjhk','NjhhMWQ5MTAwMDBjOWNkMDRhZjQwNTgwOGQ5YTllNjAwYzEyYzI5MTp7ImVtYWlsX2lkIjoiYWRtaW5AZ21haWwuY29tIiwiX2F1dGhfdXNlcl9oYXNoIjoiODkyNTFlNzZmOTlmOGZmYmM2MGQ5NWQ5NThmYTk4OGJhMWU0Y2M5NyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjQiLCJuYW1lIjoic2FrZXQgIn0=','2015-10-14 11:39:23');
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

-- Dump completed on 2016-05-20 13:50:37
