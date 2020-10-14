

"""
登录-页面
"""

from Common.basepage import BasePage

class LoginPage(BasePage):

    #登录操作
    def user_login(self,username,passwd):

        doc = ""
        self.wait_eleVisible()
        self.input_text()
        self.input_text()
        self.click_element()
