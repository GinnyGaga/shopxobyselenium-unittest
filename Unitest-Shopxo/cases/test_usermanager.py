"""============用户管理模块==============="""
import time
from cases.logincommon import LoginCommon
from po.Usermanage import User_Manager


class TestCaseUm(LoginCommon):
    """执行用户管理模块用例"""
    def test_03_um(self):
        aa = User_Manager(self.driver)
        aa.u_lick(15817216135)
        c = aa.dy()
        self.assertIn(15817216135,c.text)  #####
        print("03用户管理-搜索成功")

        time.sleep(5)