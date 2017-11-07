from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from article_app.models import Category, Article, ArticleComment, Ads
from publication.models import News, NewsComment
from opinion.models import Opinion, OpinionComment

admin.site.site_header = 'BuguPress'
admin.site.site_title = 'BuguPress'

admin.site.unregister(Group)


class AdsAdmin(admin.ModelAdmin):
    list_display = '__unicode__ title  type'.split()
    list_editable = 'type'.split()


admin.site.register(Ads, AdsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = '__unicode__ name slug'.split()
    list_editable = 'slug'.split()


admin.site.register(Category, CategoryAdmin)


class ArticleInline(admin.StackedInline):
    model = ArticleComment
    fields = ['author', 'text']
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = 'published important author title category type image date body audio keys'.split()
    list_display = '__unicode__ icon published date view category'.split()
    list_per_page = 20
    readonly_fields = 'date'.split()
    list_filter = 'date category published'.split()
    list_editable = 'category'.split()
    inlines = [ArticleInline]

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Photo</p>'

    icon.allow_tags = True


admin.site.register(Article, ArticleAdmin)


class CommentInline(admin.StackedInline):
    model = NewsComment
    fields = ['author', 'text']
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    fields = 'published title image category type body date audio keys'.split()
    list_display = '__unicode__ icon category type published date view'.split()
    list_per_page = 20
    readonly_fields = 'date'.split()
    list_filter = 'date published'.split()
    list_editable = 'published'.split()
    inlines = [CommentInline]

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Photo</p>'

    icon.allow_tags = True


admin.site.register(News, NewsAdmin)
admin.site.register(NewsComment)


# Register your models here.


class OpinionInline(admin.StackedInline):
    model = OpinionComment
    fields = ['author', 'text']
    extra = 1


class OpinionAdmin(admin.ModelAdmin):
    fields = 'published title author date body keys'.split()
    list_display = '__unicode__ icon published date view'.split()
    list_per_page = 20
    readonly_fields = 'date'.split()
    list_filter = 'date published'.split()

    inlines = [OpinionInline]

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Photo</p>'

    icon.allow_tags = True


admin.site.register(Opinion, OpinionAdmin)
# admin.site.register(OpinionInline)
