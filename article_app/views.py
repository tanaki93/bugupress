# coding=utf-8
from django.shortcuts import render

# Create your views here.
from article_app.models import Article, Category, ArticleComment, Ads
from article_app.forms import CommentForm
from opinion.models import Opinion
from gallery.models import Gallery
from publication.models import News
from itertools import chain


def category(request, category_id):
    context = dict(
        category_name=Category.objects.get(id=category_id).name,
        category_contains=sorted(
            chain(
                News.objects.filter(published=True, category_id=category_id),
                Article.objects.filter(published=True, category_id=category_id)
            ),
            key=lambda instance: instance.date, reverse=True
        ),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:]
    )
    return render(request, 'category.html', context)


def index(request):
    context = dict(
        news=News.objects.filter(published=True),
        articles=Article.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],
        kabar=Article.objects.filter(image__isnull=False, published=True, important=True)[0:3],
        first=Category.objects.order_by('slug')[0:2], second=Category.objects.order_by('slug')[0:4],
        third=Category.objects.order_by('slug')[4:5], gallery=Gallery.objects.all()[0:5],
        categories=Category.objects.all()[0:2], categories2=Category.objects.all()[2:],
        opinions=Opinion.objects.all()[0:3], )
    try:
        context['ad1'] = Ads.objects.filter(type='1')[0]
    except:
        pass
    try:
        context['infographics'] = Article.objects.filter(published=True, type="Инфографика")[0:3]
    except:
        pass
    try:
        context['ad2'] = Ads.objects.filter(type='2')[0]
    except:
        pass
    try:
        context['ad5'] = Ads.objects.filter(type='3')[0]
    except:
        pass
    return render(request, 'base.html', context)


def article(request, article_id):
    article_one = Article.objects.get(id=article_id)
    article_one.rating += 1
    article_one.save()
    context = dict(
        news=News.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        ),
        article=article_one,
        comments=ArticleComment.objects.filter(relation_id=article_id),
        other=Article.objects.filter(published=True, category_id=article_one.category_id)[0:12])
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.relation_id = article_id
            post.save()
            form = CommentForm()
            context['form'] = form
            return render(request, 'article.html', context)
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
    return render(request, 'article.html', context)


def kyrgyzstan(request):
    context = dict(
        inplace=sorted(
            chain(
                News.objects.filter(published=True, type="Кыргызстан"),
                Article.objects.filter(published=True, type="Кыргызстан")
            ),
            key=lambda instance: instance.date, reverse=True
        ),

        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],

    )

    return render(request, 'kyrgyzstan.html', context)


def world(request):
    context = dict(
        inplace=sorted(
            chain(
                News.objects.filter(published=True, type="Дүйнө"),
                Article.objects.filter(published=True, type="Дүйнө")
            ),
            key=lambda instance: instance.date, reverse=True
        ),

        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],

    )

    return render(request, 'world.html', context)


def infographics(request):
    context = dict(
        inplace=sorted(
            chain(
                Article.objects.filter(published=True, type="Инфографика")
            ),
            key=lambda instance: instance.date, reverse=True
        ),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],

    )

    return render(request, 'infographics.html', context)


def search(request):
    context = dict(
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],
    )
    if request.method == 'POST':
        context['inplace'] = sorted(
            chain(
                News.objects.filter(published=True, title__contains=request.POST['q']),
                Article.objects.filter(published=True, title__contains=request.POST['q']),
                Opinion.objects.filter(published=True, title__contains=request.POST['q'])
            ),
            key=lambda instance: instance.date, reverse=True
        )
        context['q'] = request.POST['q']
    return render(request, 'search.html', context)
