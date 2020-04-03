from utils.selenium_tools import find_element
class User_Manager():
    def __init__(self,driver):
        self.umanager = ("xpath",'//*[@id="admin-offcanvas"]/div/ul/li[5]/a/span[2]')
        self.ulist = ("xpath",'//*[@id="power-menu-126"]/li[1]/a')
        self.fr1 = ("id",'ifcontent')
        self.ss =("xpath","/html/body/div[1]/div/form/div/div/input")
        self.sc = ("xpath",'/html/body/div[1]/div/form/div/div/span/button')
        self.qr = ("xpath",'/html/body/div[1]/div/table/tbody/tr/td[2]')

        self.driver = driver

    def u_lick(self,phone):
        """
            用户操作的步骤
        """
        find_element(self.driver, self.umanager).click() # 点击用户管理
        find_element(self.driver, self.ulist).click()    # 点击用户列表
        sw_fr1 = find_element(self.driver, self.fr1)
        self.driver.switch_to_frame(sw_fr1)          # 切换作用域
        find_element(self.driver,self.ss).send_keys(phone) # 输入电话号码搜索
        find_element(self.driver,self.sc).click()  # 点击搜索

    def dy(self):
        find_element(self.driver,self.qr)




