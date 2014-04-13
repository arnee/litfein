# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.background_image'
        db.add_column(u'page_page', u'background_image',
                      self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.background_image'
        db.delete_column(u'page_page', u'background_image_id')


    models = {
        u'form_designer.form': {
            'Meta': {'object_name': 'Form'},
            'config_json': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        u'page.applicationcontent': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'ApplicationContent', 'db_table': "u'page_page_applicationcontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parameters': ('feincms.contrib.fields.JSONField', [], {'null': 'True'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'applicationcontent_set'", 'to': u"orm['page.Page']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'urlconf_path': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'page.formcontent': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'FormContent', 'db_table': "u'page_page_formcontent'"},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'page_formcontent_related'", 'to': u"orm['form_designer.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'formcontent_set'", 'to': u"orm['page.Page']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_form_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'success_message': ('django.db.models.fields.TextField', [], {})
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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'background_image': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': u"orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'navigation_extension': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['page.Page']"}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            u'template_key': ('django.db.models.fields.CharField', [], {'default': "'one-col'", 'max_length': '255'}),
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