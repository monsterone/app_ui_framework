

import pytest

class TestLogin:

    def test_login_success(self):
        """
        登录页-登录（成功）
        步骤：
            1.登录页-输入用户名
            2.登录页-输入密码
            3.登录页-点击登录
        断言：登录状态
        :return:
        """