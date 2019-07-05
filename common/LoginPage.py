from . import getLocator
from selenium import webdriver
import configparser

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        config_file_name = './config/element.ini'
        config_file = open(config_file_name, 'r')
        self.config = configparser.ConfigParser()
        self.config.read_file(config_file)

    def username(self):
        element = self.driver.find_element(getLocator(self.config.get("loginPage","user")))
        return element

    def passwd(self):
        element = self.driver.find_element(getLocator(self.config.get("loginPage", "passwd")))
        return element

    def submit(self):
        element = self.driver.find_element(getLocator(self.config.get("loginPage", "submit")))
        return element