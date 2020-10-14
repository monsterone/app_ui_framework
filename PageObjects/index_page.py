

"""
首页-页面
"""

# 判断登录状态
def get_loginStatus():
    # 获取当前app的登录状态。已登录为True，未登录为False
    try:
        # 等待5秒， #找登录注册按钮
        return False  # 未登录
    except:
        return True   # 已登录