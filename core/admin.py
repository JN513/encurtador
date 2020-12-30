from django.contrib import admin
from .models import Url

# Register your models here.

class Urls(admin.ModelAdmin):
    list_display = ('id','full_url','short_url')
    list_display_links = ('id','full_url','short_url')
    search_fields = ('id','full_url','short_url','clicks','created')
    list_per_page = 20

admin.site.register(Url, Urls)