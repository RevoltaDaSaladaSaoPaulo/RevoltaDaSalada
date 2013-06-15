# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FacebookPost.id'
        db.alter_column(u'RevoltaDaSalada_facebookpost', 'id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True))

        # Changing field 'InstagramPost.min_tag_id'
        db.alter_column(u'RevoltaDaSalada_instagrampost', 'min_tag_id', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'InstagramPost.id'
        db.alter_column(u'RevoltaDaSalada_instagrampost', 'id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True))

        # Changing field 'TwitterPost.id'
        db.alter_column(u'RevoltaDaSalada_twitterpost', 'id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'FacebookPost.id'
        db.alter_column(u'RevoltaDaSalada_facebookpost', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

        # Changing field 'InstagramPost.min_tag_id'
        db.alter_column(u'RevoltaDaSalada_instagrampost', 'min_tag_id', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'InstagramPost.id'
        db.alter_column(u'RevoltaDaSalada_instagrampost', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

        # Changing field 'TwitterPost.id'
        db.alter_column(u'RevoltaDaSalada_twitterpost', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        u'RevoltaDaSalada.facebookpost': {
            'Meta': {'object_name': 'FacebookPost'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'RevoltaDaSalada.instagrampost': {
            'Meta': {'object_name': 'InstagramPost'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'RevoltaDaSalada.twitterpost': {
            'Meta': {'object_name': 'TwitterPost'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'original_id': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['RevoltaDaSalada']