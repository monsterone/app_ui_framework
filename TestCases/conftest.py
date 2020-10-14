

import pytest
import yaml

from Common.basepage import BasePage

from Common.dir_config import caps_dir
from appium import webdriver
from PageObjects.Comm_Bus import CommBus

# 登录用例使用的前置后置
@pytest.fixture()
def startApp():
    # 准备服务器参数，与appium server连接,noRest=True
    driver = baseDriver()
    #1、要不要判断欢迎页面是否存在？
    CommBus(driver).do_welcome()
    #2、要不要判断当前用户是否登录？  --接口(可以)
    #3、如果已登录，那么先退出       --接口(可以)



#除登录以外，通用的前置条件
@pytest.fixture()
def loginApp():
    # 准备服务器参数，与appium server连接
    driver = baseDriver()
    # 1、要不要判断欢迎页面是否存在？
    CommBus(driver).do_welcome()
    # 2、要不要判断当前用户是否登录？如果没有登录，则进行登录操作
    # 3、是否有设置手势密码的框，如果有不设置

# desired_caps读取
def baseDriver(server_port=4723,noReset=None,automationName=None,**kwargs):
    # 将默认的配置数据读取出来
    fs = open(caps_dir+"/caps.yaml")
    desired_caps = yaml.load(fs)
    # 调整参数
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName
    # kwargs
    desired_caps.update(kwargs)

    # 返回一个启动对象 - driver
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)
    return driver