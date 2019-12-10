import unittest
# 创建测试套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")
# # 测试报告
with open("./report/report.html",'wb')as f:
    HTMLTestRunner(stream=f).run(suite)

#
# unittest.TextTestRunner.run(suite)


