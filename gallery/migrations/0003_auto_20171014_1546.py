# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-14 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20170706_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
