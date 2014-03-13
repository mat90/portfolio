#-*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render
from apps.site.models import Content, Images


class Home(View):
    template_name = "base.html"

    def get(self, request):
        content = Content.objects.filter(is_main=True)
        if len(content) > 0:
            for i in range(len(content)):
                content[i].images = Images.objects.filter(content=content[i])
        return render(
            request,
            self.template_name, {
                'content': content,
        })