from django.contrib import admin

# Register your models here.
from gallery.models import Gallery, Video


class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = 'date'.split()

admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Video)
