from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models import permalink
from django.template.defaultfilters import slugify

# Create your models here.

class Data4(models.Model):
	about = models.TextField()
	what_we_do = models.TextField()
	story = models.TextField()
	manifesto = models.TextField()
	team = models.TextField()
	work = models.TextField()
	economic = models.TextField()
	geolocation = models.TextField()
	comunication = models.TextField()
	management = models.TextField()

class UserProfile(models.Model):
	Genders = (
		('Male', 'Male'),
		('Female','Female'),
		)
	Positions = (
		('Software Engineer','Software Engineer'),
		('Project Mananger','Project Mananger'),
		('Analyst','Analyst'),
		('Designer','Designer'),
		('Administrator','Administrator'),
		('Director','Director'),
		)
	user = models.OneToOneField(User)
	birthday = models.DateField()
	employment = models.CharField(max_length=30, choices=Positions)
	gender = models.CharField(max_length=6, choices=Genders)
	twitter = models.URLField(max_length=1000, blank=True, null=True)
	skype = models.CharField(max_length=100, blank=True, null=True)
	linkdin = models.URLField(max_length=1000, blank=True, null=True)
	telephone = models.BigIntegerField()
	cellphone = models.BigIntegerField()
	about = models.TextField()
	profile_picture = models.ImageField(upload_to='user_img', blank=True)

	def __unicode__(self):
		return u'%s, %s' % (self.user.first_name, self.user.last_name)

class Jobs(models.Model):
	Positions = (
		('Software Engineer','Software Engineer'),
		('Project Mananger','Project Mananger'),
		('Analyst','Analyst'),
		('Designer','Designer'),
		('Administrator','Administrator'),
		('Director','Director'),
		)
	Level = (
		('Low','Low'),
		('Medium','Medium'),
		('High','High'),
		)
	posted = models.DateField()
	title = models.CharField(max_length=300)
	area = models.CharField(max_length=30, choices=Positions)
	english_level = models.CharField(max_length=10, choices=Level)
	relocation = models.BooleanField()
	formalities = models.TextField()
	description = models.TextField()
	requeriments = models.TextField()
	benefits = models.TextField()
	salary = models.BigIntegerField()
	to_begin_in = models.DateField()
	contract_type = models.CharField(max_length=150)
	contact = models.ForeignKey(UserProfile)
	phone = models.BigIntegerField()
	email = models.EmailField(max_length=350)

	def __unicode__(self):
		return u'%s, %s, %s' % (self.title, self.area, self.salary)

class Clients(models.Model):
	company_name = models.CharField(max_length=150)
	company_RP = models.CharField(max_length=150)
	company_website = models.URLField(max_length=1000, blank=True, null=True)
	company_address = models.CharField(max_length=100)
	company_country = models.CharField(max_length=100)
	company_associated_date = models.DateField()
	logo = models.ImageField(upload_to='clients_img', blank=True)

	def __unicode__(self):
		return u'%s, %s' % (self.company_name, self.company_country)

class Category(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return u'%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, { 'slug': self.slug })

class Projects(models.Model):
	project_name = models.CharField(max_length=100)
	resume = models.CharField(max_length=1000, null=True, blank=True)
	description = models.TextField()
	mandated = models.ForeignKey(UserProfile, related_name='mandated')
	members = models.ManyToManyField(UserProfile, related_name='members')
	start_date = models.DateField()
	finish_date = models.DateField()
	project_url = models.URLField(max_length=1000, blank=True, null=True)
	tags = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='projects_img', blank=True)
	company = models.ForeignKey(Clients)
	category = models.ForeignKey(Category)

	def get_members(self):
		return self.members.all()

	def __unicode__(self):
		return u'%s, %s, %s' % (self.project_name, self.company, self.mandated)

class SnapShoots(models.Model):
	snapshoot_img = models.ImageField(upload_to='snapshoots_projects_img')
	project = models.ForeignKey(Projects)

	def __unicode__(self):
		return u'%s' % (self.project)

class Blog(models.Model):
	creator = models.ManyToManyField(UserProfile)
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	tags = models.TextField()
	posted = models.DateField(blank=True, null=True)
	modified = models.DateTimeField()
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to='blogs_img', blank=True)

	def get_creator(self):
		return self.creator.all()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Blog, self).save(*args, **kwargs)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.posted = datetime.date.today()
		self.modified = datetime.datetime.today()
		return super(Blog, self).save(*args, **kwargs)

	def __unicode__(self):
		return u'%s, %s' % (self.title, self.creator)

	#@permalink
	#def get_absolute_url(self):
	#	return ('view_blog_post', None, { 'slug': self.slug })
