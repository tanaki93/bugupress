# coding=utf-8
from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
from redactor.fields import RedactorField

from publication.models import image_upload_to
from embed_video.fields import EmbedVideoField


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Фото-Отчет'
        verbose_name_plural = 'Фото-Отчеты'
        ordering = '-date'.split()
    image = models.ImageField(upload_to=image_upload_to,null=True)
    name = models.CharField(max_length=100, verbose_name='Название')

    foto_text = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Фото-Отчет',null=True)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_time(self):
        now = datetime.datetime.now()
        if date(now, 'Y.m.d') == date(self.date, 'Y.m.d'):
            return date(self.date + datetime.timedelta(hours=6), 'Бүгүн - H:i')
        elif date(now - datetime.timedelta(days=1), 'Y.m.d') == date(self.date, 'Y.m.d'):
            return 'Кечээ - %s' % date(self.date + datetime.timedelta(hours=6), 'H:i')
        else:
            return date(self.date, 'Y.m.d - H:i')

    def get_date(self):
        return self.date

    def get_text(self):
        return '%s...' % self.body[0:50]
        # return '%s...' % re.match(r'(?:[^.:;]+[.:;]){2}', self.body).group()

    def save(self, *args, **kwargs):
        self.formatted_date = self.get_time()
        self.api_category = self.category.name
        self.api_type = self.type
        super(Article, self).save()


class Video(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    url = EmbedVideoField()
    description = models.CharField(max_length=100,verbose_name='Описание')

    def __unicode__(self):
        return self.description

