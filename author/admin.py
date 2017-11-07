from django.contrib import admin

# Register your models here.
from author.models import Author

class AuthorAdmin(admin.ModelAdmin):
    fields = 'user image name about'.split()
    list_display = 'name about'.split()
    list_per_page = 20
    list_filter = 'name'.split()
    list_editable = 'name'.split()


admin.site.register(Author, AuthorAdmin)
