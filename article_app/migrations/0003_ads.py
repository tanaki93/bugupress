# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-06 20:22
from __future__ import unicode_literals

import article_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0002_auto_20170706_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('link', models.URLField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('image', models.FileField(null=True, upload_to=article_app.models.image_upload_to, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('type', models.CharField(choices=[('1', '\u0413\u043b\u0430\u0432\u043d\u0430\u044f 1'), ('2', '\u0413\u043b\u0430\u0432\u043d\u0430\u044f 2'), ('3', '\u0421\u0442\u0430\u0442\u044c\u044f 1'), ('4', '\u0421\u0442\u0430\u0442\u044c\u044f 2')], max_length=100, null=True, verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f')),
            ],
            options={
                'db_table': 'ads',
                'verbose_name': '\u0420\u0435\u043a\u043b\u0430\u043c\u0430',
                'verbose_name_plural': '\u0420\u0435\u043a\u043b\u0430\u043c\u0430',
            },
        ),
    ]
