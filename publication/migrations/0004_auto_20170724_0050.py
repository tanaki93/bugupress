# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-23 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_auto_20170714_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]