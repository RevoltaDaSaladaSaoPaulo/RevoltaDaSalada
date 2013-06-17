# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FacebookPost.real_type'
        db.add_column(u'RevoltaDaSalada_facebookpost', 'real_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=11, to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Adding field 'InstagramPost.real_type'
        db.add_column(u'RevoltaDaSalada_instagrampost', 'real_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=9, to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Adding field 'TwitterPost.real_type'
        db.add_column(u'RevoltaDaSalada_twitterpost', 'real_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=10, to=orm['contenttypes.ContentType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FacebookPost.real_type'
        db.delete_column(u'RevoltaDaSalada_facebookpost', 'real_type_id')

        # Deleting field 'InstagramPost.real_type'
        db.delete_column(u'RevoltaDaSalada_instagrampost', 'real_type_id')

        # Deleting field 'TwitterPost.real_type'
        db.delete_column(u'RevoltaDaSalada_twitterpost', 'real_type_id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'original_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '800'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'original_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '800'}),
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