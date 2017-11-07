# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-24 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0005_auto_20170724_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('text', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('relation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opinion.Opinion')),
            ],
            options={
                'db_table': 'opinion_comment',
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
    ]
