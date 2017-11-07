# coding=utf-8
from itertools import chain
from drf_multiple_model.views import MultipleModelAPIView
from rest_framework import pagination
from rest_framework import serializers
from tastypie.constants import ALL
from tastypie.resources import ModelResource

from article_app.models import Article
from gallery.models import Gallery
from opinion.models import Opinion
from publication.models import News


class BasicPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class TextAPIView(MultipleModelAPIView):
    queryList = (
        (Article.objects.filter(type=u'Кыргызстан', published=True), PlaySerializer),
        (News.objects.filter(type=u'Кыргызстан', published=True), PoemSerializer),
    )
    flat = True
    pagination_class = BasicPagination


class TextAPIView2(MultipleModelAPIView):
    def get_queryList(self):
        title = self.request.query_params['q']

        queryList = (
            (Article.objects.filter(published=True, title__contains=title), PlaySerializer),
            (News.objects.filter(published=True, title__contains=title), PoemSerializer),
        )
        return queryList

    flat = True


class TextAPIView1(MultipleModelAPIView):
    queryList = (
        (Article.objects.filter(type=u'Дүйнө', published=True), PlaySerializer),
        (News.objects.filter(type=u'Дүйнө', published=True), PoemSerializer),
    )
    flat = True
    pagination_class = BasicPagination


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.filter(published=True)
        resource_name = 'article'
        filtering = {
            'title': ALL
        }


class NewsResource(ModelResource):
    class Meta:
        queryset = News.objects.filter(published=True)
        resource_name = 'news'
        filtering = {
            'title': ALL
        }


class OpinionResource(ModelResource):
    class Meta:
        queryset = Opinion.objects.filter(published=True)
        resource_name = 'opinion'
        filtering = {
            'title': ALL
        }


class GalleryResource(ModelResource):
    class Meta:
        queryset = Gallery.objects.all()
        resource_name = 'gallery'
        filtering = {
            'title': ALL
        }


class InfoResource(ModelResource):
    class Meta:
        queryset = Article.objects.filter(published=True, type=u'Инфографика')
        resource_name = 'info'
        filtering = {
            'title': ALL
        }
