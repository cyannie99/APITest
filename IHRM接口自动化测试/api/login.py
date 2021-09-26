import requests
import app


# 导包
# 定义接口类
class LoginAPI:
    # 初始化
    def __init__(self):
        self.url = app.BASE_URL + "/api/sys/login"

    # 定义接口调用方法
    def login(self, login_data):

        return requests.post(url=self.url, json=login_data)
