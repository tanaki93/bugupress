# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-05 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
