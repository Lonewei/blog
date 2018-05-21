# _*_ coding: utf-8 _*_
__author__ = 'onewei'
__date__ = '2018/5/7 14:41'

import xadmin
from xadmin import views
from index.models import Banner, My_imgae
# 后台标题

# 后台底标


class BannerAdmin(object):
    # 设置显示内容
    list_display = ['image', 'author', 'title', 'text','time','order','is_banner']
    # 设置搜索内容
    search_fields = ['author', 'title', 'time']
    # 设置过滤器
    list_filter = ['image', 'author', 'title', 'text','time','order']
    # 指定字段为只读属性
    readonly_fields = ['time']
    # 数据即时编辑
    # 列表中直接进行修改操作
    list_editable = ['is_banner']

xadmin.site.register(Banner, BannerAdmin)