#-*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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


class Works(View):
    def get(self, request):
        works = Content.objects.filter(is_main=False)
        for w in works:
            w.images = Images.objects.filter(content=w)

        return render(
            request,
            "works.html",{
            'works': works,
        })

class Work(View):
    def get(self, id, request):
        id = int(id)
        return render(
            request,
            "work.html",
            {}
        )


class Contact(View):
    def post(self, request):
        return HttpResponseRedirect(reverse('home'))
