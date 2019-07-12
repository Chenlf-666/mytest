# -*- coding: utf-8 -*-
import configparser
import logging.config

def get_config():
    config_file_name = './config/config.ini'
    # config_file = open(config_file_name, 'r')
    config = configparser.ConfigParser()
    config.read(config_file_name, encoding="utf-8-sig")
    baseurl = config.get("base", "baseurl")
    username = config.get("base", "user")
    passwd = config.get("base", "passwd")

    return baseurl, username, passwd

def get_logger():
    logging.config.fileConfig("./config/logging.conf")
    logger = logging.getLogger("mytest")
    return logger