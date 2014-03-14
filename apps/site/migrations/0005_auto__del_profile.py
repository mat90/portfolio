# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'site_profile')


    def backwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'site_profile', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email_embed', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'site', ['Profile'])


    models = {
        u'site.content': {
            'Meta': {'object_name': 'Content'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'site.images': {
            'Meta': {'object_name': 'Images'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'to': u"orm['site.Content']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['site']