"""
# 1、封装基本函数 - 执行日志、异常处理、失败截图
#2、所以页面公共部分（不是基于业务）
"""
import os,sys

from appium.webdriver.common.mobileby import MobileBy

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.logger import Logger
from Common import dir_config
import datetime
import time

logger = Logger(__name__).getlog()
class BasePage:

    def __init__(self,driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self,locator,times=30,poll_frequency=0.5,doc=""):
        """
        等待元素可见
        :param locator: 定位元素。(元素等位类型，元素定位方式)
        :param times: 超时时间
        :param poll_frequency: 轮询时间
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        logger.info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,times,poll_frequency).until(
                EC.visibility_of_element_located(locator))
            #结束等待的时间
            end = datetime.datetime.now()
            wait_time = (end-start).seconds
            #求一个差值，写在日志当中。等待了多久。
            logger.info("{0}:元素{1}已可见，等待起始时间：{2}，等待结束时间：{3}等待时长为：{4}".format(doc,locator,start,end,wait_time))
        except:
            #捕获异常到日志
              logger.exception("等待元素可见失败！！！")
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
              self.save_screenshot(doc)
              raise


    #等待元素存在
    def wait_elePresence(self):
        pass

    #查找元素
    def get_element(self,locator,doc=""):
        logger.info("查找元素：{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logger.exception("查找元素失败!!!")
            #截图
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=""):
        #找元素
        ele = self.get_element(locator,doc)
        #元素操作
        logger.info("{0} 点击元素：{1}".format(doc,locator))
        try:
            ele.click()
        except:
            logger.exception("元素点击失败!!!")
            #截图
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 输入操作
        logger.info("{0} 元素输入：{1}".format(doc, locator))
        try:
            ele.send_keys(text)
        except:
            logger.exception("元素输入失败!!!")
            # 截图
            self.save_screenshot(doc)
            raise


    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logger.info("{0} 获取元素：{1}的文本内容".format(doc, locator))
        try:
            return ele.text
        except:
            logger.exception("获取元素的文本内容失败!!!")
            # 截图
            self.save_screenshot(doc)
            raise

        #获取元素的属性
    def get_element_attribute(self,locator,attr,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logger.info("{0} 获取元素：{1}的属性".format(doc, locator))
        try:
            return ele.get_attribute(attr)
        except:
            logger.exception("获取元素的属性失败!!!")
            # 截图
            self.save_screenshot(doc)
            raise

    #alert处理
    def alert_action(self,action="accept"):
        pass

    #iframe切换
    def switch_iframe(self,iframe_reference):
        pass

    #上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    # 截图
    def save_screenshot(self,doc=""):
        #图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        #filepath=指定的图片保存目录/model(页面功能名称)_当前时间到秒.png
        filePath = dir_config.screenshot_dir + \
            "/{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        #截图文件保存在 Screenshot目录下
        #driver方法：self.driver.save_screenshot()
        try:
            self.driver.save_screenshot(filePath)
            logger.info("截取网页成功，图片路径为{}".format(filePath))
        except:
            logger.exception("截图失败！！！")
            raise


    # 上下左右滑动
    def sliding_screen(self,direction, n=1,doc=""):
        '''
       滑屏操作
       :param direction: 滑屏方向：上-up；下-down；左-left；右-right
       :param n: 滑动次数，默认为1
       :param img_doc: 截图说明
       :return:
      '''
        size = self.driver.get_window_size()
        try:
            logger.info("开始向{}方向滑动{}次".format(direction, n))
            for i in range(n):
                time.sleep(0.5)
                if direction.lower() == 'up':
                    self.driver.swipe(start_x=size['width'] * 0.5,
                                 start_y=size['height'] * 0.9,
                                 end_x=size['width'] * 0.5,
                                 end_y=size['height'] * 0.1,
                                 duration=200)
                elif direction.lower() == 'down':
                    self.driver.swipe(start_x=size['width'] * 0.5,
                                 start_y=size['height'] * 0.1,
                                 end_x=size['width'] * 0.5,
                                 end_y=size['height'] * 0.9,
                                 duration=200)
                elif direction.lower() == 'left':
                    self.driver.swipe(start_x=size['width'] * 0.9,
                                 start_y=size['height'] * 0.5,
                                 end_x=size['width'] * 0.1,
                                 end_y=size['height'] * 0.5,
                                 duration=200)
                elif direction.lower() == 'right':
                    self.driver.swipe(start_x=size['width'] * 0.1,
                                 start_y=size['height'] * 0.5,
                                 end_x=size['width'] * 0.9,
                                 end_y=size['height'] * 0.5,
                                 duration=200)
                else:
                    logger.error("方向选择错误！")
        except Exception as e:
            logger.error("向{}方向滑动屏幕失败！".format(direction))
            # save_screenshot(img_doc)
            raise e

    # tost操作
    def is_toast_exist(slef, text,doc, timeout=30, poll_frequency=0.5):
        '''is toast exist, return True or False
        :Agrs: - driver - 传driver
        - text   - 页面上看到的文本内容
        - timeout - 最大超时时间，默认30s
        - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage: is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = (MobileBy.XPATH, "//*[contains(@text,'%s')]" % text)
            WebDriverWait(slef.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            # return True
            return slef.driver.find_element(*toast_loc).text
        except:
            logger.error("tost 获取失败！")
            slef.save_screenshot(doc)


     #获取整个屏幕大小
    def get_size(self):
        return self.driver.get_window_size()


    # H5 切换






