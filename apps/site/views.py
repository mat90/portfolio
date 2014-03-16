#-*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

import sys
import logging
import sleekxmpp
if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')

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
        works = Content.objects.filter(is_main=False).order_by('position')
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


class XMPPBot(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password, recipient, message):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.recipient = recipient
        self.msg = message
        self.add_event_handler("session_start", self.start, threaded=True)
        self.add_event_handler('message', self.message)

    def message(self, msg):
        if msg['type'] in ('normal', 'chat'):
            print msg['body']
            msg.reply("Thanks for sending:\n%s" % msg['body']).send()

    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.send_message(mto=self.recipient,
                          mbody=self.msg,
                          mtype='chat')
        self.disconnect(wait=True)

class SaveMessage(View):
    def post(self, request):
        message = MessagesForm(request.POST)
        url = request.META.get('HTTP_REFERER').split('/')
        search_result = [i for i in ['X','V'] if i in url]
        if len(search_result)>0:
            url.remove(search_result[0])
        if message.is_valid():
            message = message.save()

            jid = "sleekxmpp@creep.im"
            password = "sleekxmpp"
            to = "raven@autistici.org"
            message_text = "%s [%s]\n\n%s\n\n%s" % (message.title, message.date, message.content, message.email)
            xmpp = XMPPBot(jid, password, to, message_text)
            #xmpp.register_plugin('xep_0030') # Service Discovery
            #xmpp.register_plugin('xep_0199') # XMPP Ping
            if xmpp.connect():
                xmpp.process(block=True)


            return HttpResponseRedirect('/'.join(url)+'V')
        else:
            return HttpResponseRedirect('/'.join(url)+'X')


