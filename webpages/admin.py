from django.contrib import admin
from . import models
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id','myphoto', 'first_name', 'role', 'created_at')
    list_display_links = ('first_name', 'role', 'created_at', 'id',)
    search_fields = ('first_name',)

admin.site.register(models.Slider)
admin.site.register(models.Team, TeamAdmin)