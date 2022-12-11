from django.contrib import admin

from .models import Convert


class ConvertAdmin(admin.ModelAdmin):
    fields = ['yt_url', 'email']


admin.site.register(Convert)
