# coding=utf-8
import itertools
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

# Create your views here.
from gallery.models import Video, Gallery
from publication.forms import CommentForm
from publication.models import News, NewsComment
from itertools import chain
from article_app.models import Article, Category, Ads
from opinion.models import Opinion
from submitstory.models import Story


def kabar(request, kabar_id):
    news = News.objects.get(id=kabar_id)
    news.rating += 1
    news.save()
    context = dict(
        news=News.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date,
            reverse=True
        )[0:],
        kabar=news,
        comments=NewsComment.objects.filter(relation_id=kabar_id),
        other=sorted(
            chain(
                News.objects.filter(published=True, category_id=news.category_id),
                Article.objects.filter(published=True, category_id=news.category_id)
            ),
            key=lambda instance: instance.date)[0:12]
    )
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.relation_id = kabar_id
            post.save()
            form = CommentForm()
            context['form'] = form
            return render(request, 'news.html', context)
    else:
        form = CommentForm()
        context['form'] = form
    try:
        context['ad3'] = Ads.objects.filter(type='4')[0]
    except:
        pass
    try:
        context['ad4'] = Ads.objects.filter(type='5')[0]
    except:
        pass
    return render(request, 'news.html', context)


def main_info(request):
    all = itertools.chain(
        News.objects.filter(published=True)[0:5],
        Article.objects.filter(published=True).exclude(type=u'Инфографика')[0:5],
        Video.objects.all()[0:3],
        Article.objects.filter(type=u'Инфографика')[0:4]
    )
    result = serializers.serialize('json', all)
    return HttpResponse(result, 'application/json')


def create_story(request):
    name = request.GET.get('name')
    title = request.GET.get('title')
    phone = request.GET.get('phone')
    text = request.GET.get('text')
    story = Story.objects.create(name=name, title=title, phone=phone, text=text)
    story.save()
    return JsonResponse(dict(result = 'success'))