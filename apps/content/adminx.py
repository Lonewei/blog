# _*_ coding: utf-8 _*_
import xadmin

__author__ = 'onewei'
__date__ = '2018/5/7 15:25'
from content.models import Article
class ArticleAdmin(object):
    # 设置显示内容
    list_display = ['article_author', 'article_category', 'article_create_time', 'article_title','article_tag']
    # 设置搜索内容
    search_fields = ['article_author', 'article_category', 'article_tag']
    # 设置过滤器
    list_filter = ['article_author', 'article_category', 'article_tag']
    # 指定字段为只读属性
    readonly_fields = ['article_create_time']
    # 设置ueditor样式
    style_fields = {"article_content": "ueditor"}

xadmin.site.register(Article, ArticleAdmin)
