# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-07 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_banner_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad'),
        ),
    ]
