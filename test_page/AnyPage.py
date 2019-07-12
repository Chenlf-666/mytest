# -*- coding: utf-8 -*-
from common import getLocator,CommonConf
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser,traceback

class AnyPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = CommonConf.get_logger()
        config_file_name = './config/element.ini'
        self.config = configparser.ConfigParser()
        self.config.read(config_file_name, encoding="utf-8-sig")
        self.wait = WebDriverWait(self.driver, 5)

    def userinfo(self):
        try:
            key, value = getLocator.getLocInfo(self.config.get("anyPage", "userinfo"))
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        element = self.driver.find_element(key, value)
        return element

    def logout(self):
        try:
            key, value = getLocator.getLocInfo(self.config.get("anyPage", "logout"))
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        # element = self.driver.find_element(key, value)
        element = self.wait.until(EC.element_to_be_clickable((key, value)), "Get LogoutButton Time Out")
        return element
