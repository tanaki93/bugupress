# coding=utf-8
from django.shortcuts import render, redirect

from opinion.forms import CommentForm
from opinion.models import Opinion, OpinionComment
from opinion.forms import AddForm
from article_app.models import Article, Category, Ads
from gallery.models import Gallery
from author.models import Author
from publication.models import News
from itertools import chain
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib.auth.models import User


# Create your views here.

def allopinions(request):
    context = dict(
        opinions=Opinion.objects.filter(published=True),
        news=News.objects.filter(published=True), articles=Article.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],
        kabar=Article.objects.filter(image__isnull=False, published=True)[0:1],
        first=Category.objects.order_by('slug')[0:2], second=Category.objects.order_by('slug')[2:4],
        third=Category.objects.order_by('slug')[4:5], gallery=Gallery.objects.all()[0:5],
        categories=Category.objects.all()
    )

    return render(request, 'opinion/opinions.html', context)


def opinion(request, opinion_id):
    opinion_one = Opinion.objects.get(id=opinion_id)
    opinion_one.rating += 1
    opinion_one.save()
    context = dict(
        news=News.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],
        opinion=opinion_one,
        other=Article.objects.filter(published=True)[0:4],
        comments=OpinionComment.objects.filter(relation_id=opinion_id)
    )
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.relation_id = opinion_id
            post.save()
            form = CommentForm()
            context['form'] = form
            return render(request, 'opinion/opinion.html', context)
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
    return render(request, 'opinion/opinion.html', context)


def login(request):
    context = dict(
        news=News.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            )
        )[0:]
    )
    context.update(csrf(request))
    return render(request, 'opinion/login.html', context)


def authorization(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/opinion/list/')
    else:
        return redirect('/login/')


def list(request):
    context = dict(
        news=News.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],
        list=Opinion.objects.filter(author__user=request.user)
    )
    return render(request, 'opinion/list.html', context)


def add(request):
    context = dict(
        news=News.objects.filter(published=True),
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date, reverse=True
        )[0:],
    )
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = Author.objects.get(user=request.user).id
            post.save()
            form = AddForm()
            context['form'] = form
            return redirect('/opinion/list/')
    else:
        form = AddForm()
        context['form'] = form
    return render(request, 'opinion/new_opinion.html', context)


def delete(request, opinion_id):
    Opinion.objects.get(id=opinion_id).delete()
    return redirect('/opinion/list/')
