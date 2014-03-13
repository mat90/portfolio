#-*- coding: utf-8 -*-
from django import forms
from apps.site.models import Content, Images


class ContentForm(forms.ModelForm):
    class Meta:
        model=Content


class ImagesForm(forms.ModelForm):
    class Meta:
        model=Images

