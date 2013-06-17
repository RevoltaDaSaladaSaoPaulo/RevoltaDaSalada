# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InstagramPost'
        db.create_table(u'RevoltaDaSalada_instagrampost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('author_thumbnail_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('original_id', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('min_tag_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['InstagramPost'])

        # Adding model 'TwitterPost'
        db.create_table(u'RevoltaDaSalada_twitterpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('author_thumbnail_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('original_id', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['TwitterPost'])

        # Adding model 'FacebookPost'
        db.create_table(u'RevoltaDaSalada_facebookpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('author_thumbnail_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('original_id', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('image_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('video_url', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['FacebookPost'])


    def backwards(self, orm):
        # Deleting model 'InstagramPost'
        db.delete_table(u'RevoltaDaSalada_instagrampost')

        # Deleting model 'TwitterPost'
        db.delete_table(u'RevoltaDaSalada_twitterpost')

        # Deleting model 'FacebookPost'
        db.delete_table(u'RevoltaDaSalada_facebookpost')


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