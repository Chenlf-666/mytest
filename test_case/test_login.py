from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,traceback
import time,sys
from test_page.LoginPage import LoginPage
from test_page.AnyPage import AnyPage
from common import CommonConf

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.baseurl, self.username, self.passwd = CommonConf.get_config()
        self.logger = CommonConf.get_logger()
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
        self.logger.info("Init Class: %s" % self.__name__)

    def setUp(self) -> None:
        # print('\n' + "Test start====================")
        self.driver.get(self.baseurl)
        # self.driver.maximize_window()

    def test_1_login_success(self):
        # time.sleep(5)
        self.logger.info("Init Function: %s" % sys._getframe().f_code.co_name)
        username, passwd = self.username, self.passwd
        driver = self.driver
        wait = self.wait
        Page = LoginPage(driver)

        # wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'登录')]")))
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

        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "useractionbtn")))
        except:
            self.logger.error("Login Failed")
            self.logger.error(traceback.format_exc())
        time.sleep(3)

    def test_2_login_fail(self):
        self.logger.info("Init Function: %s" % sys._getframe().f_code.co_name)
        username, passwd = self.username, self.passwd
        driver = self.driver
        wait = self.wait
        Page = LoginPage(driver)

        # wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'登录')]")), "Login Time Out")
        button_login = Page.login()
        button_login.click()

        input_username = Page.username()
        input_username.clear()
        input_username.send_keys(username)
        input_passwd = Page.passwd()
        input_passwd.clear()
        input_passwd.send_keys("chenchen")
        button_submit = Page.submit()
        button_submit.click()

        try:
            error_alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-error")))
            error_content = error_alert.text
            self.assertEquals(error_content, "无效的登录信息")
        except:
            self.logger.error("页面源码中不存在该关键字")
            self.logger.error(traceback.format_exc())

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
        driver = self.driver
        if self.is_element_present(By.CLASS_NAME, "useractionbtn"):
            print("has login in, logouting")
            Page = AnyPage(driver)
            button_userinfo = Page.userinfo()
            button_userinfo.click()
            button_logout = Page.logout()
            time.sleep(1)
            button_logout.click()
            time.sleep(1)
            if self.is_element_present(By.CLASS_NAME, "useractionbtn"):
                self.logger.error("Logout Failed")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()
        self.logger.info("End Class: %s" % self.__name__)