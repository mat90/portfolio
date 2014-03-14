# -*- coding: UTF-8 -*-
from django.contrib import admin
from apps.site.models import Content, Positions, Profile
from apps.site.forms import ContentForm, PositionsForm, ProfileForm


class PositionsInline(admin.StackedInline):
    model=Positions
    form=PositionsForm
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
    inlines=[PositionsInline]


class ProfileAdmin(admin.ModelAdmin):
    form=ProfileForm


admin.site.register(Content, ContentAdmin)
admin.site.register(Profile, ProfileAdmin)
