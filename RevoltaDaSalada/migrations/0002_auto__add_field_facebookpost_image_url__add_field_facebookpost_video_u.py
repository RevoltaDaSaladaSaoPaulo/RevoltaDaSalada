# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FacebookPost.image_url'
        db.add_column(u'RevoltaDaSalada_facebookpost', 'image_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FacebookPost.video_url'
        db.add_column(u'RevoltaDaSalada_facebookpost', 'video_url',
                      self.gf('django.db.models.fields.TextField')(default=12),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FacebookPost.image_url'
        db.delete_column(u'RevoltaDaSalada_facebookpost', 'image_url')

        # Deleting field 'FacebookPost.video_url'
        db.delete_column(u'RevoltaDaSalada_facebookpost', 'video_url')


    models = {
        u'RevoltaDaSalada.facebookpost': {
            'Meta': {'object_name': 'FacebookPost'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video_url': ('django.db.models.fields.TextField', [], {})
        },
        u'RevoltaDaSalada.instagrampost': {
            'Meta': {'object_name': 'InstagramPost'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'RevoltaDaSalada.twitterpost': {
            'Meta': {'object_name': 'TwitterPost'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['RevoltaDaSalada']