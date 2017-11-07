# coding=utf-8
from __future__ import unicode_literals
from article_app.models import Category
from django.db import models

# Create your models here.
from redactor.fields import RedactorField
import datetime
from django.template.defaultfilters import date, slugify

# Create your models here.
from author.models import Author


def image_upload_to(instance, filename):
    return "images/%s" % filename


class News(models.Model):
    class Meta:
        db_table = 'news'
        ordering = ['-date']
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"

    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    body = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    CHOICES = (
        ('Кыргызстан', 'Кыргызстан'),
        ('Дүйнө', 'Дүйнө')
    )
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='Картинка')
    audio = models.FileField(upload_to=image_upload_to, null=True, blank=True)
    view = models.IntegerField(default=0)
    api_category = models.CharField(blank=True, null=True, max_length=100)
    api_type = models.CharField(blank=True, null=True, max_length=100)
    formatted_date = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, choices=CHOICES, null=True)
    rating = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата')
    keys = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Ключи')
    published = models.BooleanField(blank=True, default=False, verbose_name='Опубликован')

    def __unicode__(self):
        return self.title

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

    def save(self, *args, **kwargs):
        self.formatted_date = self.get_time()
        self.api_category = self.category.name
        self.api_type = self.type
        super(News, self).save()

    def get_text(self):
        return self.body[0:50] + '...'


class NewsComment(models.Model):
    class Meta:
        db_table = 'news_comment'
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"

    author = models.CharField(max_length=100, verbose_name="Ваше имя")
    text = models.TextField(verbose_name="Комментарий")
    time = models.DateTimeField(auto_now_add=True)
    relation = models.ForeignKey(News)

    @property
    def get_date(self):
        now = datetime.datetime.now()
        data = '%s-%s' % (date(now, 'Y/m/d'), date(now, 'H:i'))
        return data
