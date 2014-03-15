#-*- coding: utf-8 -*-
from django import forms
from apps.site.models import Content, Positions, Profile, Messages


class ContentForm(forms.ModelForm):
    class Meta:
        model=Content


class PositionsForm(forms.ModelForm):
    class Meta:
        model=Positions


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile

class MessagesForm(forms.ModelForm):
    class Meta:
        model=Messages
    def __init__(self, *args, **kwargs):
        super(MessagesForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})


