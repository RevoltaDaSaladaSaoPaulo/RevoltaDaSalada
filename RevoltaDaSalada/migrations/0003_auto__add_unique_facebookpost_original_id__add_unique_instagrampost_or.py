# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'FacebookPost', fields ['original_id']
        db.create_unique(u'RevoltaDaSalada_facebookpost', ['original_id'])

        # Adding unique constraint on 'InstagramPost', fields ['original_id']
        db.create_unique(u'RevoltaDaSalada_instagrampost', ['original_id'])

        # Adding unique constraint on 'TwitterPost', fields ['original_id']
        db.create_unique(u'RevoltaDaSalada_twitterpost', ['original_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TwitterPost', fields ['original_id']
        db.delete_unique(u'RevoltaDaSalada_twitterpost', ['original_id'])

        # Removing unique constraint on 'InstagramPost', fields ['original_id']
        db.delete_unique(u'RevoltaDaSalada_instagrampost', ['original_id'])

        # Removing unique constraint on 'FacebookPost', fields ['original_id']
        db.delete_unique(u'RevoltaDaSalada_facebookpost', ['original_id'])


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
            'original_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '800'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
            'original_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '800'}),
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
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'original_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '800'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['RevoltaDaSalada']