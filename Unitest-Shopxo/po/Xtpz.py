"""=============系统配置模块-后台配置==============="""
from utils.selenium_tools import find_element
class Xtpz():
    def __init__(self,driver):
        self.xtpz = ("xpath",'//*[@id="admin-offcanvas"]/div/ul/li[2]/a')
        self.dhgl = ("xpath",'//*[@id="power-menu-41"]/li[1]/a')
        self.htpz = ("xpath",'//*[@id="power-menu-41"]/li[2]/a')
        self.sdxx = ("xpath",'//*[@id="power-menu-41"]/li[3]/a/span')

        self.driver = driver

    def c_lick(self):
        """
            用户操作的步骤
        """
        find_element(self.driver, self.xtpz).click() # 点击系统配置
        find_element(self.driver, self.dhgl).click() # 点击导航管理
        find_element(self.driver, self.htpz).click() # 点击后台配置
        find_element(self.driver, self.sdxx).click() # 点击商店信息