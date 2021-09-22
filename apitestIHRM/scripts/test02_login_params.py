# 导包
import json
import unittest
from api.login import LoginAPI
from parameterized import parameterized


# 构造测试数据
def build_data():
    test_data = []
    file = "../data/login.json"
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            login_data = case_data.get("login_data")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            msg = case_data.get("message")
            test_data.append((login_data,status_code, success, code, msg))
    return test_data


# 创建测试类
class Login_param(unittest.TestCase):
    def setUp(self):
        self.api_login = LoginAPI()

    # 登录成功
    @parameterized.expand(build_data())
    def test_login(self, login_data, status_code, success, code, msg):
        # 发登录请求并断言
        response = self.api_login.login(login_data)
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("message"))
