# -*- coding: utf-8 -*-

import sys, os, time
import configparser
from selenium import webdriver

config_file_name = './config/config.ini'
config_file = open(config_file_name, 'r')
config = configparser.ConfigParser()
config.read_file(config_file)

baseurl = config.get("base","baseurl")
#print(baseurl)
browser = webdriver.Chrome()
browser.get(baseurl)
time.sleep(10)
browser.close()
config_file.close()