/*
Navicat MySQL Data Transfer

Source Server         : local-mysql
Source Server Version : 50615
Source Host           : localhost:3306
Source Database       : demo

Target Server Type    : MYSQL
Target Server Version : 50615
File Encoding         : 65001

Date: 2013-12-17 12:35:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `book`
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `tags` varchar(128) DEFAULT NULL,
  `creatorId` int(11) NOT NULL,
  `regdate` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of book
-- ----------------------------

-- ----------------------------
-- Table structure for `booknote`
-- ----------------------------
DROP TABLE IF EXISTS `booknote`;
CREATE TABLE `booknote` (
  `bookid` int(11) NOT NULL,
  `noteid` int(11) NOT NULL,
  UNIQUE KEY `primarykey` (`bookid`,`noteid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of booknote
-- ----------------------------

-- ----------------------------
-- Table structure for `bookuser`
-- ----------------------------
DROP TABLE IF EXISTS `bookuser`;
CREATE TABLE `bookuser` (
  `bookid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `role` tinyint(4) NOT NULL,
  UNIQUE KEY `primarykey` (`bookid`,`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bookuser
-- ----------------------------

-- ----------------------------
-- Table structure for `note`
-- ----------------------------
DROP TABLE IF EXISTS `note`;
CREATE TABLE `note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ntype` tinyint(4) NOT NULL,
  `content` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of note
-- ----------------------------

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(64) NOT NULL,
  `sexy` tinyint(4) DEFAULT '0',
  `email` varchar(128) NOT NULL,
  `regdate` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `avatar` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
