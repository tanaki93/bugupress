# coding=utf-8
from __future__ import unicode_literals

import datetime
from operator import attrgetter
from django.db import models
from django.template.defaultfilters import date
from redactor.fields import RedactorField
from article_app.models import Category
from author.models import Author
from django.contrib.auth.models import User


def dead_date():
    return datetime.datetime.now() - datetime.timedelta(days=31)


def image_upload_to(instance, filename):
    return "images/%s" % filename


# Create your models here.
class Opinion(models.Model):
    class Meta:
        db_table = 'opinion_opinion'
        ordering = ['-date']
        verbose_name = u"Мнение"
        verbose_name_plural = u"Мнения"

    CHOICES = (
        ('Кыргызстан', 'Кыргызстан'),
        ('Дүйнө', 'Дүйнө')
    )
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    body = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    rate = models.IntegerField(default=0)
    api_type = models.CharField(blank=True, null=True, max_length=100)
    view = models.IntegerField(default=0, verbose_name='Просмотры')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата', auto_now_add=True)
    keys = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Ключи')
    published = models.BooleanField(blank=True, default=True, verbose_name='Опубликован')
    is_opinion = models.BooleanField(blank=True, default=True)
    author = models.ForeignKey(Author, null=True)
    formatted_date = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_date(self):
        return self.date

    def get_time(self):
        now = datetime.datetime.now()
        if date(now, 'Y.m.d') == date(self.date, 'Y.m.d'):
            return date(self.date + datetime.timedelta(hours=6), 'Бүгүн - H:i')
        elif date(now - datetime.timedelta(days=1), 'Y.m.d') == date(self.date, 'Y.m.d'):
            return 'Кечээ - %s' % date(self.date + datetime.timedelta(hours=6), 'H:i')
        else:
            return date(self.date, 'Y.m.d - H:i')

    def save(self, *args, **kwargs):
        self.formatted_date = self.get_time()
        self.api_type = self.author.name
        super(Opinion, self).save()


class OpinionComment(models.Model):
    class Meta:
        db_table = 'opinion_comment'
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"

    author = models.CharField(max_length=100, verbose_name="Ваше имя")
    text = models.TextField(verbose_name="Комментарий")
    time = models.DateTimeField(auto_now_add=True)
    relation = models.ForeignKey(Opinion, null=True, blank=True)

    @property
    def get_time(self):
        now = datetime.datetime.now()
        data = '%s-%s' % (date(now, 'Y/m/d'), date(now, 'H:i'))
        return data

    def get_date(self):
        return self.date
