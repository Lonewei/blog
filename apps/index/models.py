# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from users.models import UserProfile


# Create your models here.


class Banner(models.Model):
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    author = models.ForeignKey(UserProfile, max_length=50, verbose_name=u'轮播作者')
    title = models.CharField(max_length=50, verbose_name=u'轮播内容标题')
    text = models.CharField(max_length=50, verbose_name=u'轮播内容')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'发表时间')
    order = models.IntegerField(default=100, verbose_name=u'轮播顺序')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")


    class Meta:
        verbose_name = u'首页轮播'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.author, self.title)


class My_imgae(models.Model):
    image = models.ImageField(upload_to="my_image", verbose_name=u'个人头像', max_length=100)
