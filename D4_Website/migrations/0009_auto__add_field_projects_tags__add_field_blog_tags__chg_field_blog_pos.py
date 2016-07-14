# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Projects.tags'
        db.add_column(u'D4_Website_projects', 'tags',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blog.tags'
        db.add_column(u'D4_Website_blog', 'tags',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


        # Changing field 'Blog.posted'
        db.alter_column(u'D4_Website_blog', 'posted', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Projects.tags'
        db.delete_column(u'D4_Website_projects', 'tags')

        # Deleting field 'Blog.tags'
        db.delete_column(u'D4_Website_blog', 'tags')


        # Changing field 'Blog.posted'
        db.alter_column(u'D4_Website_blog', 'posted', self.gf('django.db.models.fields.DateField')(default=0))

    models = {
        u'D4_Website.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.Category']"}),
            'creator': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['D4_Website.UserProfile']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'posted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'tags': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'D4_Website.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'D4_Website.clients': {
            'Meta': {'object_name': 'Clients'},
            'company_RP': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'company_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_associated_date': ('django.db.models.fields.DateField', [], {}),
            'company_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'D4_Website.data4': {
            'Meta': {'object_name': 'Data4'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'comunication': ('django.db.models.fields.TextField', [], {}),
            'economic': ('django.db.models.fields.TextField', [], {}),
            'geolocation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'management': ('django.db.models.fields.TextField', [], {}),
            'manifesto': ('django.db.models.fields.TextField', [], {}),
            'story': ('django.db.models.fields.TextField', [], {}),
            'team': ('django.db.models.fields.TextField', [], {}),
            'what_we_do': ('django.db.models.fields.TextField', [], {}),
            'work': ('django.db.models.fields.TextField', [], {})
        },
        u'D4_Website.jobs': {
            'Meta': {'object_name': 'Jobs'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'benefits': ('django.db.models.fields.TextField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.UserProfile']"}),
            'contract_type': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '350'}),
            'english_level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'formalities': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {}),
            'posted': ('django.db.models.fields.DateField', [], {}),
            'relocation': ('django.db.models.fields.BooleanField', [], {}),
            'requeriments': ('django.db.models.fields.TextField', [], {}),
            'salary': ('django.db.models.fields.BigIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'to_begin_in': ('django.db.models.fields.DateField', [], {})
        },
        u'D4_Website.projects': {
            'Meta': {'object_name': 'Projects'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.Category']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.Clients']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mandated': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mandated'", 'to': u"orm['D4_Website.UserProfile']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': u"orm['D4_Website.UserProfile']"}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'D4_Website.snapshoots': {
            'Meta': {'object_name': 'SnapShoots'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.Projects']"}),
            'snapshoot_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'D4_Website.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'cellphone': ('django.db.models.fields.BigIntegerField', [], {}),
            'employment': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkdin': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'profile_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.BigIntegerField', [], {}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['D4_Website']