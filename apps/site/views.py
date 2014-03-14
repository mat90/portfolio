#-*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from apps.site.models import Content, Positions, Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class Home(View):
    template_name = "base.html"

    def get(self, request):
        content = Content.objects.filter(is_main=True)
        if len(content) > 0:
            for i in range(len(content)):
                content[i].positions = Positions.objects.filter(content=content[i])
        return render(
            request,
            self.template_name, {
                'content': content,
        })


class Works(View):
    template_name = "works.html"
    def get(self, request):
        works = Content.objects.filter(is_main=False)
        for w in works:
            w.positions = Positions.objects.filter(content=w)

        return render(
            request,
            self.template_name,{
            'works': works,
        })

class Work(View):
    template_name = "work.html"

    def get(self, request, id):
        work = get_object_or_404(Content, id=int(id))
        work.positions = Positions.objects.filter(content=work)
        return render(
            request,
            self.template_name,{
            'work': work,
        })


class Contact(View):
    def post(self, request):

        return HttpResponseRedirect(reverse('home'))


class About(View):
    template_name = "about.html"

    def get(self, request):
        user = User.objects.filter(is_superuser=True)[0]
        profile = Profile.objects.get(user=user)
        return render(
            request,
            self.template_name, {
            'user': user,
            'profile': profile,
        })
