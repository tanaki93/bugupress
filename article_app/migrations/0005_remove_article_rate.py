# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-19 18:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0004_auto_20170714_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='rate',
        ),
    ]