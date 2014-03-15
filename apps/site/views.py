#-*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from apps.site.models import Content, Positions, Profile
from apps.site.forms import MessagesForm


class Home(View):
    template_name = "base.html"

    def get(self, request, status=None):
        content = Content.objects.filter(is_main=True)
        if len(content) > 0:
            for i in range(len(content)):
                content[i].positions = Positions.objects.filter(content=content[i])
        return render(
            request,
            self.template_name, {
                'status': status,
                'contact_form': MessagesForm(),
                'content': content,
        })


class Works(View):
    template_name = "works.html"
    def get(self, request, status=None):
        works = Content.objects.filter(is_main=False)
        for w in works:
            w.positions = Positions.objects.filter(content=w)

        return render(
            request,
            self.template_name,{
            'status': status,
            'contact_form': MessagesForm(),
            'works': works,
        })

class Work(View):
    template_name = "work.html"

    def get(self, request, id, status=None):
        work = get_object_or_404(Content, id=int(id))
        work.positions = Positions.objects.filter(content=work)
        return render(
            request,
            self.template_name,{
            'status': status,
            'contact_form': MessagesForm(),
            'work': work,
        })


class SaveMessage(View):
    def post(self, request):
        message = MessagesForm(request.POST)
        url = request.META.get('HTTP_REFERER').split('/')
        url.remove([i for i in ['X','V'] if i in url][0])
        if message.is_valid():
            message.save()
            return HttpResponseRedirect('/'.join(url)+'V')
        else:
            return HttpResponseRedirect('/'.join(url)+'X')


class About(View):
    template_name = "about.html"

    def get(self, request, status=None):
        user = User.objects.filter(is_superuser=True)[0]
        profile = Profile.objects.get(user=user)
        return render(
            request,
            self.template_name, {
            'status': status,
            'contact_form': MessagesForm(),
            'user': user,
            'profile': profile,
        })
