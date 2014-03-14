#-*- coding: utf-8 -*-
from django.db import models
from apps.site.messages import messages as msgs
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name=msgs['USER'],
    )
    description = models.TextField(
        verbose_name=msgs['DESCRIPTION'],
    )
    city = models.CharField(
        max_length=150,
        verbose_name=msgs['CITY'],
    )
    phone = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=msgs['PHONE'],
    )
    email_embed = models.TextField(
        verbose_name=msgs['EMAIL_EMBED'],
    )
    photo = models.ImageField(
        upload_to='upload/',
        null=True,
        blank=True,
        verbose_name=msgs['PHOTO'],
    )
    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
    class Meta:
        verbose_name=msgs['PROFILE']
        verbose_name_plural=msgs['PROFILES']


class Content(models.Model):
    is_main = models.BooleanField(
        default=False,
        verbose_name=msgs['IS_MAIN'],
    )
    title = models.CharField(
        max_length=250,
        verbose_name=msgs['TITLE'],
    )
    meta = models.CharField(
        max_length=250,
        verbose_name=msgs['META'],
    )
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name=msgs['CONTENT']
        verbose_name_plural=msgs['CONTENTS']


class Positions(models.Model):
    content = models.ForeignKey(
        Content,
        related_name='image',
    )
    text = models.TextField(
        verbose_name=msgs['TEXT'],
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='upload/',
        verbose_name=msgs['IMAGE'],
    )
    def __unicode__(self):
        return '%s' % self.image
    class Meta:
        verbose_name=msgs['IMAGE']
        verbose_name_plural=msgs['IMAGES']
