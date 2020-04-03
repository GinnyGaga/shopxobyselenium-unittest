import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 1. 加载所有的测试用例
testcases = unittest.defaultTestLoader.discover('cases','test_*.py')

# 2. 把测试用例装在到测试套件:测试集
testsuite = unittest.TestSuite()
testsuite.addTests(testcases)

# 3.运行所有的测试用例，并且生成测试报告
title  = "shopxo测试报告"
descr = "测试报告描述"
report = "./report/report.html" #自己命名，必须以.html后缀

with open(report,"wb") as f:
    # 通过open()方法以二进制写模式('wb')打开当前目录下的report.html，如果没有，则自动创建，再把这个文件的对象给f变量
    runner = HTMLTestRunner(stream=f,title=title,description=descr) # 初始化htmltestrunner
    # 　　stream 指定测试报告文件
    # 　　title  定义测试报告的标题
    # 　　description 定义测试报告的副标题
    runner.run(testsuite)  # 使用run方法运行所有的测试集

# with open()方法,里面的参数有‘w’，‘r’，‘wb’，那么：
# w是创建新文件，r是只读取文件，wb以二进制方式创建新文件，一般是存储图片等文件。