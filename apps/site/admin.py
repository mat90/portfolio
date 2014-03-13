# -*- coding: UTF-8 -*-
from django.contrib import admin
from apps.site.models import Content, Images
from apps.site.forms import ContentForm, ImagesForm


class ImagesInline(admin.StackedInline):
    model=Images
    form=ImagesForm
    extra=2


class ContentAdmin(admin.ModelAdmin):
    form=ContentForm
    list_display_links=[
        'title'
    ]
    list_display=[
        'title',
        'is_main',
    ]
    list_filter = [
        'is_main',
    ]
    inlines=[ImagesInline]

admin.site.register(Content, ContentAdmin)