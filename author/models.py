# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User

from django.db import models


def image_upload_to(instance, filename):
    return "author/%s" % filename


class Author(models.Model):
    class Meta:
        db_table = 'author'
        ordering = ['-name']
        verbose_name = u"Автор"
        verbose_name_plural = u"Авторы"

    user = models.OneToOneField(User)
    image = models.FileField(upload_to=image_upload_to, null=True, blank=False, verbose_name='Картинка')
    name = models.CharField(max_length=1000, verbose_name='Имя')
    about = models.TextField(max_length=1000, verbose_name="Описание")

    def __unicode__(self):
        return self.name
