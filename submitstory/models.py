# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from redactor.fields import RedactorField


# Create your models here.
def image_upload_to(instance, filename):
    return "images/%s" % filename


class Story(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, null=True)
    title = models.CharField(max_length=100)
    text = RedactorField(
        upload_to=image_upload_to,
        allow_file_upload=True,
        allow_image_upload=True,
        verbose_name='Текст')

    def __unicode__(self):
        return self.title
