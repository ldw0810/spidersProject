/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50611
Source Host           : localhost:3306
Source Database       : spiders

Target Server Type    : MYSQL
Target Server Version : 50611
File Encoding         : 65001

Date: 2017-05-22 18:13:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for job_template
-- ----------------------------
DROP TABLE IF EXISTS `gufeng`;
CREATE TABLE `gufeng` (
  `ID` integer NOT NULL DEFAULT 0 COMMENT '主键',
  `NAME` varchar(255) DEFAULT NULL COMMENT '名称',
  `COVER` varchar(1000) DEFAULT NULL COMMENT '封面海报',
  `LINK` varchar(1000) DEFAULT NULL COMMENT '链接地址',
  `UPDATE_DESC` varchar(1000) DEFAULT NULL COMMENT '更新描述',
  `UPDATE_TIME` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;