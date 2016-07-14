# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Data4'
        db.create_table(u'D4_Website_data4', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('what_we_do', self.gf('django.db.models.fields.TextField')()),
            ('story', self.gf('django.db.models.fields.TextField')()),
            ('manifesto', self.gf('django.db.models.fields.TextField')()),
            ('team', self.gf('django.db.models.fields.TextField')()),
            ('work', self.gf('django.db.models.fields.TextField')()),
            ('economic', self.gf('django.db.models.fields.TextField')()),
            ('geolocation', self.gf('django.db.models.fields.TextField')()),
            ('comunication', self.gf('django.db.models.fields.TextField')()),
            ('management', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'D4_Website', ['Data4'])

        # Adding model 'UserProfile'
        db.create_table(u'D4_Website_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('employment', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('linkdin', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.BigIntegerField')()),
            ('cellphone', self.gf('django.db.models.fields.BigIntegerField')()),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('profile_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'D4_Website', ['UserProfile'])

        # Adding model 'Jobs'
        db.create_table(u'D4_Website_jobs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posted', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('english_level', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('relocation', self.gf('django.db.models.fields.BooleanField')()),
            ('formalities', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('requeriments', self.gf('django.db.models.fields.TextField')()),
            ('benefits', self.gf('django.db.models.fields.TextField')()),
            ('salary', self.gf('django.db.models.fields.BigIntegerField')()),
            ('to_begin_in', self.gf('django.db.models.fields.DateField')()),
            ('contract_type', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['D4_Website.UserProfile'])),
            ('phone', self.gf('django.db.models.fields.BigIntegerField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=350)),
        ))
        db.send_create_signal(u'D4_Website', ['Jobs'])

        # Adding model 'Clients'
        db.create_table(u'D4_Website_clients', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('company_RP', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('company_website', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('company_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_associated_date', self.gf('django.db.models.fields.DateField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'D4_Website', ['Clients'])

        # Adding model 'Projects'
        db.create_table(u'D4_Website_projects', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('mandated', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mandated', to=orm['D4_Website.UserProfile'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('finish_date', self.gf('django.db.models.fields.DateField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['D4_Website.Clients'])),
        ))
        db.send_create_signal(u'D4_Website', ['Projects'])

        # Adding M2M table for field members on 'Projects'
        m2m_table_name = db.shorten_name(u'D4_Website_projects_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projects', models.ForeignKey(orm[u'D4_Website.projects'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'D4_Website.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projects_id', 'userprofile_id'])

        # Adding model 'Category'
        db.create_table(u'D4_Website_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'D4_Website', ['Category'])

        # Adding model 'Blog'
        db.create_table(u'D4_Website_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('posted', self.gf('django.db.models.fields.DateField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['D4_Website.Category'])),
        ))
        db.send_create_signal(u'D4_Website', ['Blog'])

        # Adding M2M table for field creator on 'Blog'
        m2m_table_name = db.shorten_name(u'D4_Website_blog_creator')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm[u'D4_Website.blog'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'D4_Website.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blog_id', 'userprofile_id'])


    def backwards(self, orm):
        # Deleting model 'Data4'
        db.delete_table(u'D4_Website_data4')

        # Deleting model 'UserProfile'
        db.delete_table(u'D4_Website_userprofile')

        # Deleting model 'Jobs'
        db.delete_table(u'D4_Website_jobs')

        # Deleting model 'Clients'
        db.delete_table(u'D4_Website_clients')

        # Deleting model 'Projects'
        db.delete_table(u'D4_Website_projects')

        # Removing M2M table for field members on 'Projects'
        db.delete_table(db.shorten_name(u'D4_Website_projects_members'))

        # Deleting model 'Category'
        db.delete_table(u'D4_Website_category')

        # Deleting model 'Blog'
        db.delete_table(u'D4_Website_blog')

        # Removing M2M table for field creator on 'Blog'
        db.delete_table(db.shorten_name(u'D4_Website_blog_creator'))


    models = {
        u'D4_Website.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.Category']"}),
            'creator': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['D4_Website.UserProfile']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'posted': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
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
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['D4_Website.Clients']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mandated': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mandated'", 'to': u"orm['D4_Website.UserProfile']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members'", 'symmetrical': 'False', 'to': u"orm['D4_Website.UserProfile']"}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
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