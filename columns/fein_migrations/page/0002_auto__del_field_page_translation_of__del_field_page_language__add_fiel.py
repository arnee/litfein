# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.translation_of'
        db.delete_column(u'page_page', u'translation_of_id')

        # Deleting field 'Page.language'
        db.delete_column(u'page_page', u'language')

        # Adding field 'Page.meta_keywords'
        db.add_column(u'page_page', u'meta_keywords',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Page.meta_description'
        db.add_column(u'page_page', u'meta_description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Page.featured'
        db.add_column(u'page_page', u'featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Page.excerpt'
        db.add_column(u'page_page', u'excerpt',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Page.translation_of'
        db.add_column(u'page_page', u'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'translations', null=True, to=orm['page.Page'], blank=True),
                      keep_default=False)

        # Adding field 'Page.language'
        db.add_column(u'page_page', u'language',
                      self.gf('django.db.models.fields.CharField')(default='af', max_length=10),
                      keep_default=False)

        # Deleting field 'Page.meta_keywords'
        db.delete_column(u'page_page', u'meta_keywords')

        # Deleting field 'Page.meta_description'
        db.delete_column(u'page_page', u'meta_description')

        # Deleting field 'Page.featured'
        db.delete_column(u'page_page', u'featured')

        # Deleting field 'Page.excerpt'
        db.delete_column(u'page_page', u'excerpt')


    models = {
        u'medialibrary.category': {
            'Meta': {'ordering': "[u'parent__title', u'title']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'medialibrary.mediafile': {
            'Meta': {'ordering': "[u'-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'page.mediafilecontent': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'MediaFileContent', 'db_table': "u'page_page_mediafilecontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "u'+'", 'to': u"orm['medialibrary.MediaFile']"}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'mediafilecontent_set'", 'to': u"orm['page.Page']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        u'page.page': {
            'Meta': {'ordering': "[u'tree_id', u'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'db_index': 'True', 'blank': 'True'}),
            u'_content_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'_page_title': ('django.db.models.fields.CharField', [], {'max_length': '69', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'featured': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'navigation_extension': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['page.Page']"}),
            u'publication_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 26, 0, 0)'}),
            u'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            u'template_key': ('django.db.models.fields.CharField', [], {'default': "'base2.html'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'page.richtextcontent': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'RichTextContent', 'db_table': "u'page_page_richtextcontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'richtextcontent_set'", 'to': u"orm['page.Page']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('feincms.contrib.richtext.RichTextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['page']
