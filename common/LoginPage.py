# from . import getLocator
from selenium import webdriver
import configparser,time

from common import getLocator

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        config_file_name = '../config/element.ini'
        config_file = open(config_file_name, 'r')
        self.config = configparser.ConfigParser()
        self.config.read_file(config_file)

    def login(self):
        print(self.driver)
        print(self.config)
        print(getLocator.getLocator(self.config.get("loginPage", "login")))
        element = self.driver.find_element(getLocator.getLocator(self.config.get("loginPage", "login")))
        return element

    def username(self):
        element = self.driver.find_element(getLocator.getLocator(self.config.get("loginPage", "user")))
        return element

    def passwd(self):
        element = self.driver.find_element(getLocator(self.config.get("loginPage", "passwd")))
        return element

    def submit(self):
        element = self.driver.find_element(getLocator(self.config.get("loginPage", "submit")))
        return element

    def keyword(self):
        print(self.config.get("loginPage", "kw"))
        element = self.driver.find_element(getLocator.getLocator(self.config.get("loginPage", "kw")))
        return element

    def submit2(self):
        element = self.driver.find_element(getLocator.getLocator(self.config.get("loginPage", "su")))
        return element

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    page = LoginPage(driver)
    kw = page.keyword()
    kw.input("123123")
    sub = page.submit2()
    sub.click()
    time.sleep(30)
    driver.close()