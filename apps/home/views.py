#-*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render


class Home(View):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name, {})
