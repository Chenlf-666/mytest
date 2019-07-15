# -*- coding: utf-8 -*-
import configparser
import logging.config
from selenium.webdriver.common.by import By

class ParseConfig:
    def __init__(self):
        self.common_conf = "./config/config.ini"
        element_conf = "./config/element.ini"
        self.element_config = configparser.ConfigParser()
        self.element_config.read(element_conf, encoding="utf-8-sig")

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.common_conf, encoding="utf-8-sig")
        baseurl = config.get("base", "baseurl")
        username = config.get("base", "username")
        passwd = config.get("base", "passwd")
        return baseurl, username, passwd

    def getLocInfo(self, section, option):
        key, value = self.element_config.get(section, option).split(">")
        if not value:
            print("配置文件格式错误")

        if key == "id":
            return By.ID, value
        if key == "class":
            return By.CLASS_NAME, value
        if key == "xpath":
            return By.XPATH, value

    def get_logger(self):
        logging.config.fileConfig("./config/logging.conf")
        logger = logging.getLogger("mytest")
        return logger