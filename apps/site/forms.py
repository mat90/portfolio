#-*- coding: utf-8 -*-
from django import forms
from apps.site.models import Content, Positions, Profile


class ContentForm(forms.ModelForm):
    class Meta:
        model=Content


class PositionsForm(forms.ModelForm):
    class Meta:
        model=Positions


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
