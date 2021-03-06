# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'RevoltaDaSalada_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('author_thumbnail_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('original_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=800)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['Post'])

        # Adding model 'InstagramPost'
        db.create_table(u'RevoltaDaSalada_instagrampost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['RevoltaDaSalada.Post'], unique=True, primary_key=True)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('min_tag_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['InstagramPost'])

        # Adding model 'TwitterPost'
        db.create_table(u'RevoltaDaSalada_twitterpost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['RevoltaDaSalada.Post'], unique=True, primary_key=True)),
            ('min_tag_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['TwitterPost'])

        # Adding model 'FacebookPost'
        db.create_table(u'RevoltaDaSalada_facebookpost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['RevoltaDaSalada.Post'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('image_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'RevoltaDaSalada', ['FacebookPost'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'RevoltaDaSalada_post')

        # Deleting model 'InstagramPost'
        db.delete_table(u'RevoltaDaSalada_instagrampost')

        # Deleting model 'TwitterPost'
        db.delete_table(u'RevoltaDaSalada_twitterpost')

        # Deleting model 'FacebookPost'
        db.delete_table(u'RevoltaDaSalada_facebookpost')


    models = {
        u'RevoltaDaSalada.facebookpost': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'FacebookPost', '_ormbases': [u'RevoltaDaSalada.Post']},
            'content': ('django.db.models.fields.TextField', [], {}),
            'image_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['RevoltaDaSalada.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'RevoltaDaSalada.instagrampost': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'InstagramPost', '_ormbases': [u'RevoltaDaSalada.Post']},
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['RevoltaDaSalada.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'RevoltaDaSalada.post': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'author_thumbnail_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '800'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'RevoltaDaSalada.twitterpost': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'TwitterPost', '_ormbases': [u'RevoltaDaSalada.Post']},
            'min_tag_id': ('django.db.models.fields.BigIntegerField', [], {}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['RevoltaDaSalada.Post']", 'unique': 'True', 'primary_key': 'True'})
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