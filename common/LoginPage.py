# -*- coding: utf-8 -*-
from . import getLocator
from selenium import webdriver
import configparser,time

# from common import getLocator

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        config_file_name = './config/element.ini'
        self.config = configparser.ConfigParser()
        self.config.read(config_file_name, encoding="utf-8-sig")

    def login(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "login"))
        # print(value)
        element = self.driver.find_element(key, value)
        return element

    def username(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "user"))
        element = self.driver.find_element(key, value)
        return element

    def passwd(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "passwd"))
        element = self.driver.find_element(key, value)
        return element

    def submit(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "submit"))
        element = self.driver.find_element(key, value)
        return element

    def keyword(self):
        key, value = getLocator.getLocInfo(self.config.get("loginPage", "kw"))
        print(key, "-------------", value)
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