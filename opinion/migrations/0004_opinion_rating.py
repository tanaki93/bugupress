# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-19 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0003_opinion_formatted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
