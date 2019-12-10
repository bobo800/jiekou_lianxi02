import unittest
# 导包
import requests
# 创建测试类
import api


class ApiLogin:
    # 初始化
    def __init__(self):
        self.url = api.BASE_URL + "/api/sys/login"

#     定义请求json

    def api_login(self,mobile,password):
        # d定义请求json串
        data = {"mobile":mobile,"password":password}
        # 请求登录
        return requests.post(url=self.url,json=data , headers=api.headers)



