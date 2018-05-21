# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models
from users.models import UserProfile


# Create your models here.

class Article(models.Model):
    article_author = models.ForeignKey(UserProfile, verbose_name=u"作者")
    article_category = models.CharField(default=u"综合", max_length=50, verbose_name=u"文章类别")
    article_create_time = models.DateTimeField(default=datetime.now, verbose_name=u'发表时间')
    article_title = models.CharField(max_length=50, verbose_name=u'文章标题')
    article_content = UEditorField(verbose_name=u"文章内容", imagePath="media/ueditor/",
                                            filePath="media/ueditor/",
                                            default="")

    article_image = models.ImageField(upload_to="image/%Y/%m", verbose_name=u"文章配图", max_length=100)
    article_tag = models.CharField(max_length=20, verbose_name=u'文章标签')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.article_title
