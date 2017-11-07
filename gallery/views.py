from django.shortcuts import render

from article_app.models import Article, Category, Ads
from opinion.models import Opinion
from gallery.models import Video, Gallery
from publication.models import News
from itertools import chain
# Create your views here.

def multimedia(request):
    context = dict(
        videos=Video.objects.all(),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:]
    )

    return render(request, 'multimedia.html', context)


def gallery(request):
    context = dict(
        gallery=Gallery.objects.all(),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:]
    )

    return render(request, 'gallery.html', context)


def photo(request, id):
    context = dict(
        kabar=Gallery.objects.get(id=id),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:]
    )
    try:
        context['ad3'] = Ads.objects.filter(type='4')[0]
    except:
        pass
    try:
        context['ad4'] = Ads.objects.filter(type='5')[0]
    except:
        pass
    return render(request, 'photos.html', context)
