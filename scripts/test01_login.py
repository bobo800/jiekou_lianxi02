
import unittest
# 导包

# 创建测试类
import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取 apilogin 对象
        cls.login = ApiLogin()


    # 登录测试方法
    def test01_login(self,mobile ='13800000002', password='123456'):
        # 调用业务方法
        r = self.login.api_login(mobile, password)
        # 提取token
        token = r.json().get("data")
        api.headers['Authorization'] = "Bearer " + token
        print('登录成功后的headers值为：', api.headers)
        print(r.status_code)

#         断言
        assert_common(self,r )






