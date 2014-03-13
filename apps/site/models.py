#-*- coding: utf-8 -*-
from django.db import models
from apps.site.messages import messages as msgs


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
    text = models.TextField(
        verbose_name=msgs['TEXT'],
    )
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name=msgs['CONTENT']
        verbose_name_plural=msgs['CONTENTS']


class Images(models.Model):
    content = models.ForeignKey(
        Content,
        related_name='image',
    )
    image = models.ImageField(
        upload_to='/media/upload/',
        verbose_name=msgs['IMAGE'],
    )
    def __unicode__(self):
        return '%s' % self.image
    class Meta:
        verbose_name=msgs['IMAGE']
        verbose_name_plural=msgs['IMAGES']
