/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.7.17-log : Database - imagethinking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`imagethinking` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `imagethinking`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can add group',3,'add_group'),(9,'Can change group',3,'change_group'),(10,'Can delete group',3,'delete_group'),(11,'Can view group',3,'view_group'),(12,'Can view permission',2,'view_permission'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Bookmark',6,'add_bookmark'),(22,'Can change Bookmark',6,'change_bookmark'),(23,'Can delete Bookmark',6,'delete_bookmark'),(24,'Can add User Setting',7,'add_usersettings'),(25,'Can change User Setting',7,'change_usersettings'),(26,'Can delete User Setting',7,'delete_usersettings'),(27,'Can add User Widget',8,'add_userwidget'),(28,'Can change User Widget',8,'change_userwidget'),(29,'Can delete User Widget',8,'delete_userwidget'),(30,'Can add log entry',9,'add_log'),(31,'Can change log entry',9,'change_log'),(32,'Can delete log entry',9,'delete_log'),(33,'Can view Bookmark',6,'view_bookmark'),(34,'Can view log entry',9,'view_log'),(35,'Can view User Setting',7,'view_usersettings'),(36,'Can view User Widget',8,'view_userwidget'),(37,'Can add 新浪app',10,'add_sina_app'),(38,'Can change 新浪app',10,'change_sina_app'),(39,'Can delete 新浪app',10,'delete_sina_app'),(40,'Can add 今日头条app',11,'add_toutiao_app'),(41,'Can change 今日头条app',11,'change_toutiao_app'),(42,'Can delete 今日头条app',11,'delete_toutiao_app'),(43,'Can add 搜狐app',12,'add_souhu_app'),(44,'Can change 搜狐app',12,'change_souhu_app'),(45,'Can delete 搜狐app',12,'delete_souhu_app'),(46,'Can add 账户分析',13,'add_toutiao_ad_to_parameter'),(47,'Can change 账户分析',13,'change_toutiao_ad_to_parameter'),(48,'Can delete 账户分析',13,'delete_toutiao_ad_to_parameter'),(49,'Can add 账户分析',14,'add_toutiao_parameter'),(50,'Can change 账户分析',14,'change_toutiao_parameter'),(51,'Can delete 账户分析',14,'delete_toutiao_parameter'),(52,'Can add 账户分析',15,'add_parameter'),(53,'Can change 账户分析',15,'change_parameter'),(54,'Can delete 账户分析',15,'delete_parameter'),(55,'Can add 账户分析',11,'add_toutiao_param'),(56,'Can change 账户分析',11,'change_toutiao_param'),(57,'Can delete 账户分析',11,'delete_toutiao_param'),(58,'Can view 账户分析',15,'view_parameter'),(59,'Can view 新浪app',10,'view_sina_app'),(60,'Can view 搜狐app',12,'view_souhu_app'),(61,'Can view 账户分析',13,'view_toutiao_ad_to_parameter'),(62,'Can view 今日头条app',11,'view_toutiao_app'),(63,'Can view 账户分析',16,'view_toutiao_param'),(64,'Can view 账户分析',14,'view_toutiao_parameter'),(65,'Can add 用户信息',17,'add_userprofile'),(66,'Can change 用户信息',17,'change_userprofile'),(67,'Can delete 用户信息',17,'delete_userprofile'),(68,'Can view 用户信息',17,'view_userprofile');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(15,'media','parameter'),(10,'media','sina_app'),(12,'media','souhu_app'),(13,'media','toutiao_ad_to_parameter'),(11,'media','toutiao_app'),(16,'media','toutiao_param'),(14,'media','toutiao_parameter'),(5,'sessions','session'),(17,'users','userprofile'),(6,'xadmin','bookmark'),(9,'xadmin','log'),(7,'xadmin','usersettings'),(8,'xadmin','userwidget');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2018-09-29 09:15:02.301878'),(2,'contenttypes','0002_remove_content_type_name','2018-09-29 09:15:03.090868'),(3,'auth','0001_initial','2018-09-29 09:15:05.952409'),(4,'auth','0002_alter_permission_name_max_length','2018-09-29 09:15:06.742382'),(5,'auth','0003_alter_user_email_max_length','2018-09-29 09:15:06.803226'),(6,'auth','0004_alter_user_username_opts','2018-09-29 09:15:06.850329'),(7,'auth','0005_alter_user_last_login_null','2018-09-29 09:15:06.886638'),(8,'auth','0006_require_contenttypes_0002','2018-09-29 09:15:06.916078'),(9,'auth','0007_alter_validators_add_error_messages','2018-09-29 09:15:06.942574'),(10,'auth','0008_alter_user_username_max_length','2018-09-29 09:15:06.978883'),(11,'auth','0009_alter_user_last_name_max_length','2018-09-29 09:15:07.010288'),(12,'users','0001_initial','2018-09-29 09:15:11.527364'),(13,'admin','0001_initial','2018-09-29 09:15:13.314373'),(14,'admin','0002_logentry_remove_auto_add','2018-09-29 09:15:13.373252'),(15,'media','0001_initial','2018-09-29 09:15:13.925744'),(16,'media','0002_auto_20180502_1633','2018-09-29 09:15:21.634120'),(17,'media','0003_auto_20180502_1706','2018-09-29 09:15:45.985911'),(18,'media','0004_auto_20180503_1749','2018-09-29 09:15:46.748406'),(19,'media','0005_souhu_app','2018-09-29 09:15:47.113462'),(20,'media','0006_auto_20180508_1633','2018-09-29 09:15:51.720822'),(21,'media','0007_auto_20180509_1522','2018-09-29 09:15:52.358691'),(22,'media','0008_auto_20180811_1546','2018-09-29 09:15:53.233058'),(23,'media','0009_auto_20180811_1602','2018-09-29 09:16:16.869457'),(24,'media','0010_auto_20180813_1418','2018-09-29 09:16:18.936145'),(25,'media','0011_auto_20180929_1135','2018-09-29 09:16:19.364988'),(26,'sessions','0001_initial','2018-09-29 09:16:19.753595'),(27,'users','0002_remove_userprofile_gender','2018-09-29 09:16:20.226601'),(28,'xadmin','0001_initial','2018-09-29 09:16:23.998846'),(29,'xadmin','0002_log','2018-09-29 09:16:25.879079'),(30,'xadmin','0003_auto_20160715_0100','2018-09-29 09:16:26.533636'),(31,'users','0003_userprofile_is_paying_user','2018-09-30 03:05:12.420557'),(32,'users','0004_auto_20181009_1404','2018-10-09 06:04:58.974853');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

/*Table structure for table `parameter` */

DROP TABLE IF EXISTS `parameter`;

CREATE TABLE `parameter` (
  `id` varchar(16) NOT NULL,
  `media` varchar(64) DEFAULT NULL,
  `channel` varchar(64) DEFAULT NULL,
  `header` longtext,
  `url` longtext,
  `parameter` longtext,
  `is_active` tinyint(1) NOT NULL,
  `system` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `parameter` */

/*Table structure for table `sina_app` */

DROP TABLE IF EXISTS `sina_app`;

CREATE TABLE `sina_app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pos` varchar(500) NOT NULL,
  `newsId` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `link` varchar(500) NOT NULL,
  `pic` varchar(500) NOT NULL,
  `showTag` varchar(500) NOT NULL,
  `articlePreload` varchar(500) NOT NULL,
  `commentStatus` varchar(500) NOT NULL,
  `adid` varchar(500) NOT NULL,
  `dislikeTags` varchar(500) NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sina_app` */

/*Table structure for table `souhu_app` */

DROP TABLE IF EXISTS `souhu_app`;

CREATE TABLE `souhu_app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monitorkey` varchar(50) NOT NULL,
  `resource` longtext NOT NULL,
  `resource2` longtext NOT NULL,
  `weight` varchar(20) NOT NULL,
  `itemspaceid` varchar(20) NOT NULL,
  `resource1` longtext NOT NULL,
  `impressionid` varchar(50) NOT NULL,
  `special` longtext NOT NULL,
  `offline` varchar(80) NOT NULL,
  `adid` varchar(80) NOT NULL,
  `viewmonitor` varchar(1000) NOT NULL,
  `size` varchar(20) NOT NULL,
  `online` varchar(20) NOT NULL,
  `position` varchar(20) NOT NULL,
  `tag` varchar(20) NOT NULL,
  `editNews` varchar(10) NOT NULL,
  `statsType` varchar(5) NOT NULL,
  `isPreload` varchar(5) NOT NULL,
  `newsType` varchar(10) NOT NULL,
  `gbcode` varchar(50) NOT NULL,
  `commentNum` varchar(10) NOT NULL,
  `isHasSponsorships` varchar(5) NOT NULL,
  `recomTime` varchar(5) NOT NULL,
  `newsId` varchar(30) NOT NULL,
  `iconNight` longtext NOT NULL,
  `isWeather` varchar(5) NOT NULL,
  `isRecom` varchar(5) NOT NULL,
  `iconText` varchar(10) NOT NULL,
  `iconDay` longtext NOT NULL,
  `link` longtext NOT NULL,
  `abposition` varchar(10) NOT NULL,
  `adType` varchar(5) NOT NULL,
  `playTime` varchar(20) NOT NULL,
  `adp_type` varchar(10) NOT NULL,
  `isFlash` varchar(5) NOT NULL,
  `isHasTv` varchar(5) NOT NULL,
  `newschn` varchar(5) NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `amount` int(11) NOT NULL,
  `resource_text` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `souhu_app` */

/*Table structure for table `toutiao_ad_to_parameter` */

DROP TABLE IF EXISTS `toutiao_ad_to_parameter`;

CREATE TABLE `toutiao_ad_to_parameter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toutiao_ad_id` int(11) DEFAULT NULL,
  `toutiao_para_id` int(11) DEFAULT NULL,
  `time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `toutiao_ad_to_parameter` */

/*Table structure for table `toutiao_app` */

DROP TABLE IF EXISTS `toutiao_app`;

CREATE TABLE `toutiao_app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abstract` varchar(50) NOT NULL,
  `action_list` longtext NOT NULL,
  `aggr_type` varchar(64) NOT NULL,
  `allow_download` varchar(10) NOT NULL,
  `article_sub_type` varchar(4) NOT NULL,
  `article_tpye` varchar(4) NOT NULL,
  `article_url` longtext NOT NULL,
  `ban_comment` varchar(10) NOT NULL,
  `behot_time` varchar(20) NOT NULL,
  `bury_count` varchar(20) NOT NULL,
  `cell_flag` varchar(20) NOT NULL,
  `cell_layout_style` varchar(20) NOT NULL,
  `cell_type` varchar(20) NOT NULL,
  `comment_count` varchar(20) NOT NULL,
  `content_decoration` varchar(20) NOT NULL,
  `digg_count` varchar(20) NOT NULL,
  `display_url` varchar(1024) NOT NULL,
  `filter_words` longtext NOT NULL,
  `group_flags` varchar(20) NOT NULL,
  `group_id` varchar(50) NOT NULL,
  `has_video` varchar(10) NOT NULL,
  `hot` varchar(10) NOT NULL,
  `ignore_web_transform` varchar(10) NOT NULL,
  `is_subject` varchar(20) NOT NULL,
  `item_id` varchar(50) NOT NULL,
  `item_version` varchar(4) NOT NULL,
  `label` varchar(20) NOT NULL,
  `label_style` varchar(4) NOT NULL,
  `large_image_list` longtext NOT NULL,
  `level` varchar(4) NOT NULL,
  `log_pb` longtext NOT NULL,
  `natant_level` varchar(4) NOT NULL,
  `preload_web` varchar(4) NOT NULL,
  `publish_time` varchar(20) NOT NULL,
  `raw_ad_data` longtext NOT NULL,
  `read_count` varchar(10) NOT NULL,
  `repin_count` varchar(10) NOT NULL,
  `rid` varchar(200) NOT NULL,
  `share_count` varchar(20) NOT NULL,
  `share_info` longtext NOT NULL,
  `share_url` longtext NOT NULL,
  `show_dislike` varchar(10) NOT NULL,
  `show_portrait` varchar(10) NOT NULL,
  `show_portrait_article` varchar(10) NOT NULL,
  `source` varchar(50) NOT NULL,
  `source_avatar` varchar(100) NOT NULL,
  `tag` varchar(10) NOT NULL,
  `tag_id` varchar(50) NOT NULL,
  `title` varchar(500) NOT NULL,
  `url` longtext NOT NULL,
  `user_repin` varchar(10) NOT NULL,
  `user_verified` varchar(20) NOT NULL,
  `video_detail_info` longtext NOT NULL,
  `video_duration` varchar(10) NOT NULL,
  `video_id` varchar(50) NOT NULL,
  `video_play_info` longtext NOT NULL,
  `video_proportion_article` varchar(20) NOT NULL,
  `video_style` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `toutiao_app` */

/*Table structure for table `toutiao_parameter` */

DROP TABLE IF EXISTS `toutiao_parameter`;

CREATE TABLE `toutiao_parameter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `header` longtext,
  `url` varchar(200) DEFAULT NULL,
  `fp` varchar(60) DEFAULT NULL,
  `version_code` varchar(60) DEFAULT NULL,
  `app_name` varchar(60) DEFAULT NULL,
  `vid` varchar(60) DEFAULT NULL,
  `device_id` varchar(60) DEFAULT NULL,
  `channel` varchar(60) DEFAULT NULL,
  `resolution` varchar(60) DEFAULT NULL,
  `aid` varchar(60) DEFAULT NULL,
  `ab_version` varchar(2000) DEFAULT NULL,
  `ab_feature` varchar(60) DEFAULT NULL,
  `ab_group` varchar(60) DEFAULT NULL,
  `openudid` varchar(60) DEFAULT NULL,
  `idfv` varchar(60) DEFAULT NULL,
  `ac` varchar(60) DEFAULT NULL,
  `os_version` varchar(60) DEFAULT NULL,
  `ssmix` varchar(60) DEFAULT NULL,
  `device_platform` varchar(60) DEFAULT NULL,
  `iid` varchar(60) DEFAULT NULL,
  `ab_client` varchar(60) DEFAULT NULL,
  `device_type` varchar(60) DEFAULT NULL,
  `idfa` varchar(60) DEFAULT NULL,
  `refresh_reason` varchar(60) DEFAULT NULL,
  `detail` varchar(60) DEFAULT NULL,
  `last_refresh_sub_entrance_interval` varchar(60) DEFAULT NULL,
  `tt_from` varchar(60) DEFAULT NULL,
  `count` varchar(60) DEFAULT NULL,
  `list_count` varchar(60) DEFAULT NULL,
  `support_rn` varchar(60) DEFAULT NULL,
  `LBS_status` varchar(60) DEFAULT NULL,
  `cp` varchar(60) DEFAULT NULL,
  `loc_mode` varchar(60) DEFAULT NULL,
  `min_behot_time` varchar(60) DEFAULT NULL,
  `session_refresh_idx` varchar(60) DEFAULT NULL,
  `image` varchar(60) DEFAULT NULL,
  `strict` varchar(60) DEFAULT NULL,
  `refer` varchar(60) DEFAULT NULL,
  `city` varchar(60) DEFAULT NULL,
  `concern_id` varchar(60) DEFAULT NULL,
  `language` varchar(60) DEFAULT NULL,
  `st_time` varchar(60) DEFAULT NULL,
  `_as` varchar(60) DEFAULT NULL,
  `ts` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `toutiao_parameter` */

/*Table structure for table `users_userprofile` */

DROP TABLE IF EXISTS `users_userprofile`;

CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `is_paying_user` tinyint(1) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `principal` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `users_userprofile` */

insert  into `users_userprofile`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`,`address`,`mobile`,`is_paying_user`,`company_name`,`image`,`principal`) values (1,'pbkdf2_sha256$100000$2tUU4pqhOHq3$qZOPEd4FYsYn3df5JNaMAJghrYXqdFO6p3Bl8CUxCSU=','2018-09-29 09:32:09.628506',1,'admin','','','1@1.com',1,1,'2018-09-29 09:24:56.663181','',NULL,0,'','image/default.png','');

/*Table structure for table `users_userprofile_groups` */

DROP TABLE IF EXISTS `users_userprofile_groups`;

CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `users_userprofile_groups` */

/*Table structure for table `users_userprofile_user_permissions` */

DROP TABLE IF EXISTS `users_userprofile_user_permissions`;

CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `users_userprofile_user_permissions` */

/*Table structure for table `xadmin_bookmark` */

DROP TABLE IF EXISTS `xadmin_bookmark`;

CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `xadmin_bookmark` */

/*Table structure for table `xadmin_log` */

DROP TABLE IF EXISTS `xadmin_log`;

CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `xadmin_log` */

/*Table structure for table `xadmin_usersettings` */

DROP TABLE IF EXISTS `xadmin_usersettings`;

CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `xadmin_usersettings` */

insert  into `xadmin_usersettings`(`id`,`key`,`value`,`user_id`) values (1,'dashboard:home:pos','',1);

/*Table structure for table `xadmin_userwidget` */

DROP TABLE IF EXISTS `xadmin_userwidget`;

CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `xadmin_userwidget` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
