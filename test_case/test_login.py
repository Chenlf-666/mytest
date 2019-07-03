from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,configparser

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.baseurl, self.username, self.passwd = self.get_config(self)
        self.driver = webdriver.Chrome()

    def setUp(self) -> None:
        print("Test start")
        self.driver.get(self.baseurl)

    def test_login_success(self):
        # time.sleep(5)
        username, passwd = self.username, self.passwd
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        button_login = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'登录')]")))
        button_login.click()
        userinput = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        title = driver.title
        # self.assertEqual(title, 'PAXSTORE', 'title is wrong!')
        userinput.send_keys(username)
        driver.find_element_by_id("password").send_keys(passwd)
        driver.find_element_by_id("submitBtn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "AppListView-app-list-row")))

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
        print("Test end")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()