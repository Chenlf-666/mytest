# -*- coding: utf-8 -*-
from common import getLocator,CommonConf
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser,time,traceback

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = CommonConf.get_logger()
        config_file_name = './config/element.ini'
        self.config = configparser.ConfigParser()
        self.config.read(config_file_name, encoding="utf-8-sig")
        self.wait = WebDriverWait(self.driver, 5)

    def login(self):
        try:
            key, value = getLocator.getLocInfo(self.config.get("loginPage", "login"))
            element = self.wait.until(EC.element_to_be_clickable((key, value)), "Get LoginButton Time Out")
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def username(self):
        try:
            key, value = getLocator.getLocInfo(self.config.get("loginPage", "user"))
            element = self.driver.find_element(key, value)
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def passwd(self):
        try:
            key, value = getLocator.getLocInfo(self.config.get("loginPage", "passwd"))
            element = self.driver.find_element(key, value)
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def submit(self):
        try:
            key, value = getLocator.getLocInfo(self.config.get("loginPage", "submit"))
            element = self.driver.find_element(key, value)
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def keyword(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "kw"))
        element = self.driver.find_element(key, value)
        return element

    def submit2(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "su"))
        element = self.driver.find_element(key, value)
        return element

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    page = LoginPage(driver)
    kw = page.keyword()
    kw.send_keys("123123")
    sub = page.submit2()
    sub.click()
    time.sleep(5)
    driver.close()