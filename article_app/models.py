# coding=utf-8
from __future__ import unicode_literals
import datetime
from operator import attrgetter

from django.db import models
from django.template.defaultfilters import date

# Create your models here.
from redactor.fields import RedactorField
import re

from author.models import Author


def dead_date():
    return datetime.datetime.now() - datetime.timedelta(days=365)


def image_upload_to(instance, filename):
    return "images/%s" % filename


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"
        ordering = ['slug', '-name']

    slug = models.IntegerField(null=True, blank=True, verbose_name='Место')
    name = models.CharField(max_length=100, verbose_name="Название")
    colour = models.CharField(max_length=50, null=True, verbose_name="Цвет")

    def __unicode__(self):
        return self.name

    def get_article(self):
        return self.article_set.filter(published=True)[0:1]

    def get_articles(self):
        return self.article_set.filter(date__gte=dead_date(), published=True)[0:4]

    def get_news(self):
        return self.news_set.filter(date__gte=dead_date(), published=True)[0:4]

    def get_all(self):
        s = []
        for i in self.article_set.filter(published=True)[0:4]:
            s.append(i)
        for i in self.news_set.filter(published=True)[0:4]:
            s.append(i)
        o = tuple(sorted(s, key=attrgetter('date'), reverse=True))
        return o


class Article(models.Model):
    class Meta:
        db_table = 'article_article'
        ordering = ['-date']
        verbose_name = u"Статья"
        verbose_name_plural = u"Статьи"

    CHOICES = (
        ('Кыргызстан', 'Кыргызстан'),
        ('Дүйнө', 'Дүйнө'),
        ('Инфографика', 'Инфографика')
    )
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    image = models.FileField(upload_to=image_upload_to, null=True, blank=False, verbose_name='Картинка')
    category = models.ForeignKey(Category, verbose_name='Категория')
    type = models.CharField(max_length=100, choices=CHOICES, null=True)
    important = models.BooleanField(blank=False, default=False, verbose_name="Важно")
    author = models.ForeignKey(Author, null=True, blank=True)
    body = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')
    audio = models.FileField(upload_to=image_upload_to, null=True, blank=True, verbose_name='Аудио')
    api_category = models.CharField(blank=True, null=True, max_length=100)
    api_type = models.CharField(blank=True, null=True, max_length=100)
    formatted_date = models.CharField(max_length=100, blank=True, null=True)
    view = models.IntegerField(default=0, verbose_name='Просмотры')
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата', auto_now_add=True)
    keys = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Ключи')
    published = models.BooleanField(blank=True, default=False, verbose_name='Опубликован')
    is_article = models.BooleanField(blank=True, default=True)

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

    def get_text(self):
        return '%s...' % self.body[0:50]
        # return '%s...' % re.match(r'(?:[^.:;]+[.:;]){2}', self.body).group()

    def save(self, *args, **kwargs):
        self.formatted_date = self.get_time()
        self.api_category = self.category.name
        self.api_type = self.type
        super(Article, self).save()


class ArticleComment(models.Model):
    class Meta:
        db_table = 'article_comment'
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"

    author = models.CharField(max_length=100, verbose_name="Ваше имя")
    text = models.TextField(verbose_name="Комментарий")
    time = models.DateTimeField(auto_now_add=True)
    relation = models.ForeignKey(Article, null=True, blank=True)

    @property
    def get_time(self):
        now = datetime.datetime.now()
        data = '%s-%s' % (date(now, 'Y/m/d'), date(now, 'H:i'))
        return data

    def get_date(self):
        return self.date


class Ads(models.Model):
    class Meta:
        db_table = 'ads'
        verbose_name = u"Реклама"
        verbose_name_plural = u"Реклама"

    ADPOSITION = (
        ('1', 'Главная 1'),
        ('2', 'Главная 2'),
        ('3', 'Главная 3'),
        ('4', 'Статья 1'),
        ('5', 'Статья 2')
    )

    title = models.CharField(max_length=1000, verbose_name='Название')
    link = models.URLField(verbose_name="Ссылка")
    image = models.FileField(upload_to=image_upload_to, null=True, blank=False, verbose_name='Изображение')
    type = models.CharField(max_length=100, choices=ADPOSITION, null=True, verbose_name="Позиция")

    def __unicode__(self):
        return self.title
