


#框架项目顶层目录
# BASE_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0] #获取路径另一种方法
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


#测试数据路径
testdatas_dir = os.path.join(BASE_DIR,"TestDatas")

#测试用例路径
testcase_dir = os.path.join(BASE_DIR,"TestCases")

#测试报告输出路径
htmlreport_dir = os.path.join(BASE_DIR,"Outputs","reports")

#日志输出路径
log_dir = os.path.join(BASE_DIR,"Outputs","logs")

#截图输出路径
screenshot_dir = os.path.join(BASE_DIR,"Outputs","screenshots")


#Desired_Caps配置路径
caps_dir = os.path.join(BASE_DIR,"Desired_Caps")







# #测试报告路径
# test_report_path = os.path.join(BASE_DIR,'test_result','html_report','result.html')
#
# #配置文件的路径
# case_config_path = os.path.join(BASE_DIR,'conf','case.config')