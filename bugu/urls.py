"""bugu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings
from tastypie.api import Api

from article_app.api import NewsResource,OpinionResource, ArticleResource, GalleryResource, TextAPIView, TextAPIView1, InfoResource, \
    TextAPIView2

v1_api = Api(api_name='v1')
v2_api = Api(api_name='v2')
v1_api.register(NewsResource())
v2_api.register(ArticleResource())
v1_api.register(GalleryResource())
v1_api.register(InfoResource())
v1_api.register(OpinionResource())

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^$', 'article_app.views.index'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^a/', include(v2_api.urls)),
    url(r'^k/$', TextAPIView.as_view()),
    url(r'^d/$', TextAPIView1.as_view()),
    url(r'^query/', TextAPIView2.as_view()),
    url(r'^create_story/$', 'publication.views.create_story'),
    url(r'^kabar/(?P<kabar_id>\d+)/$', 'publication.views.kabar'),
    url(r'^article/(?P<article_id>\d+)/$', 'article_app.views.article'),
    url(r'^search/', 'article_app.views.search'),
    url(r'^opinions/', 'opinion.views.allopinions'),
    url(r'^main_info/', 'publication.views.main_info'),
    url(r'^kyrgyzstan/', 'article_app.views.kyrgyzstan'),
    url(r'^world/', 'article_app.views.world'),
    url(r'^infographics/', 'article_app.views.infographics'),
    url(r'^multimedia/', 'gallery.views.multimedia'),
    url(r'^gallery/', 'gallery.views.gallery'),
    url(r'^photos/(?P<id>\d+)/', 'gallery.views.photo'),
    url(r'^submitstory/', 'submitstory.views.submitstory'),
    url(r'^opinion/(?P<opinion_id>\d+)/$', 'opinion.views.opinion'),
    url(r'^opinion/list/$', 'opinion.views.list'),
    url(r'^opinion/add/$', 'opinion.views.add'),
    url(r'^opinion/delete/(?P<opinion_id>\d+)/$', 'opinion.views.delete'),
    url(r'^login/$', 'opinion.views.login'),
    url(r'^authorization/$', 'opinion.views.authorization'),
    url(r'^category/(?P<category_id>\d+)/$', 'article_app.views.category'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name='image_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
