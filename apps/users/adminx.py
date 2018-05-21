# _*_ coding: utf-8 _*_
__author__ = 'onewei'
__date__ = '2018/4/19 20:48'


import xadmin
from xadmin import views
from users.models import EmialCaptcha
# 后台标题
class BaseSetting(object):
    # 开启主题
    enable_themes = True
    # 设置左侧导航栏为下拉菜单
    use_bootswatch = True

# 后台底标
class GlobalSetting(object):
    site_title = "oneweicc"
    site_footer = "摇号必中摇号必中！！！"
    menu_style = "accordion"

class EmialCaptchaAdmin(object):
    # 设置显示内容
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 设置搜索内容
    search_fields = ['code', 'email', 'send_type']
    # 设置过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']
    # 指定字段为只读属性
    # readonly_fields = ['code']


xadmin.site.register(EmialCaptcha, EmialCaptchaAdmin)