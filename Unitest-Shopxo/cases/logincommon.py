
import unittest
from selenium import webdriver
from po.LoginPage import LoginPage

class LoginCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = '.\driver\\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.maximize_window()
        cls.driver.get("http://132.232.44.158:9999/shopxo/admin.php")
        print("start!")
        admin_login = LoginPage(cls.driver)
        admin_login.login("admin", "shopxo")
        print("这是登录页面")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("stop!")

