# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-22 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20171022_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
