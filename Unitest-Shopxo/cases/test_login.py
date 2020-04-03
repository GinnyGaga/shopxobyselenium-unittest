"""============验证后台登录功能=========="""
import time
import unittest
from selenium import webdriver
from po.LoginPage import LoginPage

class TestCaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = 'driver\\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.maximize_window()
        cls.driver.get("http://132.232.44.158:9999/shopxo/admin.php")
        print("start!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("stop!")

    def test_01_login(self):
        admin_login = LoginPage(self.driver)
        admin_login.login("admin", "shopxo")
        time.sleep(5)

        url = self.driver.current_url
        self.assertEqual(url,"http://132.232.44.158:9999/shopxo/admin.php?s=/index/index.html")
        print("01登录成功")


