# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Content'
        db.create_table('site_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('meta', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('site', ['Content'])

        # Adding model 'Images'
        db.create_table('site_images', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image', to=orm['site.Content'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('site', ['Images'])


    def backwards(self, orm):
        # Deleting model 'Content'
        db.delete_table('site_content')

        # Deleting model 'Images'
        db.delete_table('site_images')


    models = {
        'site.content': {
            'Meta': {'object_name': 'Content'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'site.images': {
            'Meta': {'object_name': 'Images'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'to': "orm['site.Content']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['site']