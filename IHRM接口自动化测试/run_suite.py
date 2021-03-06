# 导包
import time
import unittest
from scripts.test01_login import TestLogin
# from scripts.test02_login_params import Login_param
from scripts.test03_employee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner

# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
# 指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLTestRunner执行器
    runner = HTMLTestRunner(f, title="接口测试报告")
    # 执行测试套件
    runner.run(suite)
