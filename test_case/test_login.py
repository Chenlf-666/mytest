from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,configparser
import time
from common.LoginPage import LoginPage

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.baseurl, self.username, self.passwd = self.get_config(self)
        self.driver = webdriver.Chrome()

    def setUp(self) -> None:
        print('\n' + "Test start====================")
        self.driver.get(self.baseurl)
        # self.driver.maximize_window()

    def test_1_login_success(self):
        # time.sleep(5)
        username, passwd = self.username, self.passwd
        driver = self.driver
        Page = LoginPage(driver)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'登录')]")))
        button_login = Page.login()
        button_login.click()

        input_username = Page.username()
        input_username.clear()
        input_username.send_keys(username)
        input_passwd = Page.passwd()
        input_passwd.clear()
        input_passwd.send_keys(passwd)
        button_submit = Page.submit()
        button_submit.click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "AppListView-app-list-row")))
        assert "chentest" in driver.page_source,"login failed"
        time.sleep(5)

    def test_2_login_fail(self):
        # time.sleep(5)
        username, passwd = self.username, self.passwd
        driver = self.driver
        Page = LoginPage(driver)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'登录')]")))
        self.button_login = Page.submit()
        self.button_login.click()

        self.input_username = Page.username()
        self.input_username.clear()
        self.input_username.send_keys(username)
        self.input_passwd = Page.passwd()
        self.input_passwd.clear()
        self.input_passwd.send_keys(passwd)
        self.button_submit = Page.submit()
        self.button_submit.click()

        error_alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-error")))
        error_content = error_alert.text
        self.assertEquals(error_content, "无效的登录信息", "页面源码中不存在该关键字")
        # assert "无效的登录信息" in driver.page_source, "页面源码中不存在该关键字！"

    def get_config(self):
        config_file_name = './config/config.ini'
        config_file = open(config_file_name, 'r')
        config = configparser.ConfigParser()
        config.read_file(config_file)
        baseurl = config.get("base", "baseurl")
        username = config.get("base", "user")
        passwd = config.get("base", "passwd")
        config_file.close()
        return baseurl, username, passwd

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self) -> None:
        # print(self.driver.find_element(By.CLASS_NAME, "useractionbtn").text)
        wait = WebDriverWait(self.driver, 5)
        if self.is_element_present(By.CLASS_NAME, "useractionbtn"):
            print("has login in, logout")
            self.driver.find_element(By.CLASS_NAME, "useractionbtn").click()
            button_logout = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'登出')]")))
            button_logout.click()
        print("Test end==============")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()