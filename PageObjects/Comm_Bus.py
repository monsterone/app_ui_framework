

from Common.basepage import BasePage
import time
class CommBus(BasePage):

    # 处理欢迎页面
    def do_welcome(self,driver):
        time.sleep(7)
        # 如果没有找到首页的元素/或不包含MainActvity,那么就是在欢迎页面
        curAct = self.driver.current_activity
        if curAct.find("MainActivity") == -1: # 没有首页找到，在欢迎页面
            #滑动欢迎页面致首页
            #左划两次次，点击进入首页
            self.sliding_screen("left",2)
            # 点击进入首页

    # 是否设置手势密码
    def is_setGesture(self,acton=False):
        #有没有设置手势密码的弹框 -5秒
        # 如果有是设置还是不设置呢？
        if acton == False:
            pass # 点击不设置
        else:
            pass # 点击立即设置
