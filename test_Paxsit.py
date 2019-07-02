# -*- coding: utf-8 -*-

#coding:utf-8

import sys, os, time

from packages.HTMLTestRunner import HTMLTestRunner
import configparser,unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
config_file_name = './config/config.ini'
config_file = open(config_file_name, 'r')
config = configparser.ConfigParser()
config.read_file(config_file)

baseurl = config.get("base", "baseurl")
username = config.get("base", "user")
passwd = config.get("base", "passwd")
#print(baseurl)

class Mytest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get(baseurl)

    def test_login(self):
        #time.sleep(5)
        brower = self.browser
        wait = WebDriverWait(brower, 5)
        time.sleep(5)
        #print(brower.page_source)

        button_login = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'登录')]")))
        button_login.click()
        userinput = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        title = brower.title
        #self.assertEqual(title, 'PAXSTORE', 'title is wrong!')
        userinput.send_keys(username)
        brower.find_element_by_id("password").send_keys(passwd)
        brower.find_element_by_id("submitBtn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "AppListView-app-list-row")))


    def tearDown(self) -> None:
        self.browser.close()

config_file.close()

suite = unittest.TestSuite()
suite.addTest(Mytest("test_login"))
# with open('./report/HTMLReport.html', 'wb') as f:
#     runner = HTMLTestRunner(stream=f,title='My Test Report',
#     description='generated by HTMLTestRunner.',
#     verbosity=2)
#     runner.run(suite)
# f.close()

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)