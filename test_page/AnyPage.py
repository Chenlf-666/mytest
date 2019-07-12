# -*- coding: utf-8 -*-
from common import CommonConf
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import configparser,traceback,time

class AnyPage:
    def __init__(self, driver):
        self.driver = driver
        self.initConf = CommonConf.ParseConfig()
        self.logger = self.initConf.get_logger()
        self.wait = WebDriverWait(self.driver, 5)

    def button_userinfo(self):
        try:
            # key, value = getLocator.getLocInfo(self.config.get("anyPage", "userinfo"))
            key, value = self.initConf.getLocInfo("anyPage", "userinfo")
            element = self.driver.find_element(key, value)
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def button_logout(self):
        try:
            # key, value = getLocator.getLocInfo(self.config.get("anyPage", "logout"))
            key, value = self.initConf.getLocInfo("anyPage", "logout")
            element = self.wait.until(EC.element_to_be_clickable((key, value)))
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        # element = self.driver.find_element(key, value)
        return element

    def Action_logout(self):
        button_userinfo = self.button_userinfo()
        button_userinfo.click()
        button_logout = self.button_logout()
        time.sleep(1)
        button_logout.click()