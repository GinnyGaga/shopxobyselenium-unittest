"""=============系统配置模块==============="""
import time
from cases.logincommon import LoginCommon
from po.Xtpz import Xtpz

class TestCaseXt(LoginCommon):
    """执行系统配置模块用例"""
    def test_02_cc(self):
        aa = Xtpz(self.driver)
        aa.c_lick()
        print("02系统配置")

        time.sleep(5)