from django.shortcuts import render
from submitstory.forms import StoryForm
from django.shortcuts import redirect
from article_app.models import Article
from opinion.models import Opinion
from publication.models import News
from itertools import chain


# Create your views here.
def submitstory(request):
    context = dict(
        everything=sorted(
            chain(
                News.objects.filter(published=True),
                Article.objects.filter(published=True),
                Opinion.objects.filter(published=True)
            ),
            key=lambda instance: instance.date
        )[0:],
    )
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'story/submited.html', context)
        else:
            return render(request, 'story/failed.html', context)
    else:
        form = StoryForm()
        context['form'] = form
    return render(request, 'story/submit.html', context)
