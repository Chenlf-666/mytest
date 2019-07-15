# -*- coding: utf-8 -*-
from common import CommonConf
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import traceback

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.initConf = CommonConf.ParseConfig()
        self.baseurl, self.username, self.passwd = self.initConf.get_config()
        self.logger = self.initConf.get_logger()
        self.wait = WebDriverWait(self.driver, 5)

    def button_login(self):
        try:
            # key, value = getLocator.getLocInfo(self.config.get("loginPage", "login"))
            key, value = self.initConf.getLocInfo("loginPage", "login")
            element = self.wait.until(EC.element_to_be_clickable((key, value)))
        except ValueError as e:
            self.logger.error("get key/value error")
            self.logger.error(traceback.format_exc())
        except NoSuchElementException as e:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def input_username(self):
        try:
            # key, value = getLocator.getLocInfo(self.config.get("loginPage", "user"))
            key, value = self.initConf.getLocInfo("loginPage", "user")
            element = self.wait.until(EC.element_to_be_clickable((key, value)))
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def input_passwd(self):
        try:
            # key, value = getLocator.getLocInfo(self.config.get("loginPage", "passwd"))
            key, value = self.initConf.getLocInfo("loginPage", "passwd")
            element = self.wait.until(EC.element_to_be_clickable((key, value)))
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def button_submit(self):
        try:
            # key, value = getLocator.getLocInfo(self.config.get("loginPage", "submit"))
            key, value = self.initConf.getLocInfo("loginPage", "submit")
            element = self.driver.find_element(key, value)
        except:
            self.logger.error("get element error===>", key, "---", value)
            self.logger.error(traceback.format_exc())
        return element

    def Action_login(self):
        #初始界面的登录动作
        button_login = self.button_login()
        button_login.click()
        input_username = self.input_username()
        input_passwd = self.input_passwd()
        input_username.clear()
        input_username.send_keys(self.username)
        input_passwd.clear()
        input_passwd.send_keys(self.passwd)
        button_submit = self.button_submit()
        button_submit.submit()

    def Action_login_password_error(self):
        #初始界面的登录动作
        button_login = self.button_login()
        button_login.click()
        input_username = self.input_username()
        input_passwd = self.input_passwd()
        input_username.clear()
        input_username.send_keys(self.username)
        input_passwd.clear()
        input_passwd.send_keys("chenchen")
        button_submit = self.button_submit()
        button_submit.submit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    page = LoginPage(driver)