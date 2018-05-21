# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    image = models.ImageField(upload_to='user_image/%Y/%m', max_length=100, verbose_name=u'用户头像')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name


class EmialCaptcha(models.Model):
    code = models.CharField(max_length=50, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    is_use = models.BooleanField(default=False, verbose_name=u'激活码状态')
    send_type = models.CharField(max_length=20, choices=(("register", u"注册"), ("forget", u"找回密码"),),
                                 verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)