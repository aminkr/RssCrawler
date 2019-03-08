from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    fields = ('img_url','pub_date', 'summary','title')
    list_display = ('img_src', 'pub_date', 'summary', 'title')
    readonly_fields = ('title', 'pub_date', 'summary', 'img_url')
    list_display_links = None
    list_per_page = 5
    search_fields = ('title',)

    class Media:
        css = {
            'all': ('styles.css',)
        }

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    fields = ('name','rss_url')
    list_display = ('name','rss_url')
    readonly_fields = ('name','rss_url')
    list_display_links = None
    list_per_page = 5

    def has_add_permission(self, request, obj=None):
        return False
