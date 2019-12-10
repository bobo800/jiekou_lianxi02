import unittest
# 导包

# 创建测试类 继承unitts
import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.employee = ApiEmployee()


# 创建方法

# 新增员工
    def test01_post(self,username = "hellowordd",moblie = "18510112000",workNumber='10240000915'):
        # 调用新增接口
        r = self.employee.api_post_employee(username,moblie,workNumber)
        print("新增的员工为：",r.json())
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("新增的员工id为：",api.user_id)
        assert_common(self,r)


# 修改员工
    def test01_put(self,username = 'vovssop30'):
        r = self.employee.api_put_employee(username)
        print("修改的员工为：",r.json())


# 查询员工
    def test03_get(self):
        r = self.employee.api_get_employee()
        print("查询结果为：",r.json())


# 删除员工
    def test04_delete(self):
        r = self.employee.api_delete_employee()
        print("删除数据为：",r.json())
