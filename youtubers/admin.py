from . import models
from django.contrib import admin
from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'myphoto','name', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name', 'subs_count',)
    list_editable = ('is_featured',)

admin.site.register(models.Youtuber, YtAdmin)
