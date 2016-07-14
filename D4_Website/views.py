from django.shortcuts import render_to_response, redirect, render
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from D4_Website.models import *
from django.core import serializers
from django.db.models import Q
import simplejson
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
#from sets import Set
try:
   set
except NameError:
   from sets import Set as set

# Create your views here.

def home(request, templa_name="welcome_D4.html"):
	args = {}
	args.update(csrf(request))
	return render(request, templa_name, args)

def main(request, templa_name="home.html"):
	args = {}
	args.update(csrf(request))
	return render(request, templa_name, args)


def isotope(request, templa_name="Isotope.html"):
	args = {}
	args.update(csrf(request))
	return render(request, templa_name, args)


def us(request, templa_name="us.html"):
	info = Data4.objects.all()
	users = UserProfile.objects.all()
	clients = Clients.objects.order_by('company_name')
	args = {}
	args.update(csrf(request))
	args['info'] = info
	args['users'] = users
	args['clients'] =clients
	return render(request, templa_name, args)

def work(request, templa_name="work.html"):
	info = Data4.objects.all()
	project = Projects.objects.order_by('project_name')
	snapshoot = []
	categories = []
	for i in project:
		snapshoot = snapshoot + [SnapShoots.objects.filter(project = i.id)]
		categories = categories + [Category.objects.filter(title = i.category)]
	zipped_list = zip(project, snapshoot, categories)
	category = Category.objects.order_by('title')
	args = {}
	args.update(csrf(request))
	args['info'] = info
	args['zipped_list'] = zipped_list
	args['category'] = category
	return render(request, templa_name, args)

def category_job(request, cj, templa_name="work.html"):
	c_j = Category.objects.get(slug = cj)
	project = Projects.objects.order_by('project_name')
	info = Data4.objects.all()
	months = Blog.objects.order_by('posted').distinct('posted')
	category = Category.objects.order_by('title')
	snapshoot_p = []
	for i in project:
		snapshoot_p = snapshoot_p + [SnapShoots.objects.filter(project = i.id)]
	zipped_list = zip(project, snapshoot_p)
	project = Projects.objects.filter(category = c_j).order_by('project_name')
	snapshoot_j = []
	for i in project:
		snapshoot_j = snapshoot_j + [SnapShoots.objects.filter(project = i.id)]
	cat_job = zip(project, snapshoot_j)
	category = Category.objects.order_by('title')
	args = {}
	args.update(csrf(request))
	args['info'] = info
	args['zipped_list'] = zipped_list
	args['category'] = category
	args['cat_job'] = cat_job
	return render(request, templa_name, args)

def media(request, templa_name="media.html"):
	info = Data4.objects.all()
	blog = Blog.objects.order_by('title','-posted')
	months = Blog.objects.order_by('posted').distinct('posted')
	category = Category.objects.order_by('title')
	tag = []
	for i in blog:
		tag = tag + i.tags.split(', ')
	tag = map(str, tag)
	tag = sorted(set(tag))
	args = {}
	args.update(csrf(request))
	args['blog'] = blog
	args['months'] = months
	args['category'] = category
	args['tag'] = tag
	args['info'] = info
	return render(request, templa_name, args)

def search_post(request, templa_name="media.html"):
	keywords = request.POST['keywords'].encode("utf-8")
	k = []
	k = keywords.split(' ') + [keywords]

	try:
		kwards = {}
		args = Q()
		for x in k:
			w = '%s ' %(x)
			z = ' %s' %(x)
			y = ' %s ' %(x)
			args.add(Q(title__icontains = w)|
				 	 Q(slug__icontains = w)|
					 Q(body__icontains = w)|
					 Q(tags__icontains = w)|
					 Q(category__title__icontains = w)|
					 Q(title__icontains = z)|
				 	 Q(slug__icontains = z)|
					 Q(body__icontains = z)|
					 Q(tags__icontains = z)|
					 Q(category__title__icontains = z)|
					 Q(title__icontains = y)|
				 	 Q(slug__icontains = y)|
					 Q(body__icontains = y)|
					 Q(tags__icontains = y)|
					 Q(category__title__icontains = y), Q.OR)

		blog_list = Blog.objects.filter(*[args], **kwards).order_by('title','-posted')
	except Blog.DoesNotExist:
		pass

	u_l = []
	for x in k:
		if len(User.objects.filter(Q(first_name__icontains = x) | Q(last_name__icontains = x))) > 0:
			u_l.append(User.objects.filter(Q(first_name__icontains = x) | Q(last_name__icontains = x)).values('id'))

	user_list = []

	if len(u_l) > 0:
		u_l = u_l[0]
		for i in u_l:
			user_list = user_list + [i['id']]

	user_list = sorted(set(user_list))

	searchs_list = Blog.objects.filter(creator__in = user_list)

	searchs_list = searchs_list | blog_list

	info = Data4.objects.all()
	blog = Blog.objects.order_by('title','-posted')
	months = Blog.objects.order_by('posted').distinct('posted')
	category = Category.objects.order_by('title')
	tag = []
	for i in blog:
		tag = tag + i.tags.split(', ')
	tag = map(str, tag)
	tag = sorted(set(tag))
	args = {}
	args.update(csrf(request))
	args['blog'] = blog
	args['months'] = months
	args['category'] = category
	args['tag'] = tag
	args['info'] = info
	args['searchs_list'] = searchs_list
	return render(request, templa_name, args)

def recent_post(request, rp, templa_name="media.html"):
	r_p = rp
	rec_post = Blog.objects.get(slug = r_p)
	info = Data4.objects.all()
	blog = Blog.objects.order_by('title','-posted')
	months = Blog.objects.order_by('posted').distinct('posted')
	category = Category.objects.order_by('title')
	tag = []
	for i in blog:
		tag = tag + i.tags.split(', ')
	tag = map(str, tag)
	tag = sorted(set(tag))
	args = {}
	args.update(csrf(request))
	args['blog'] = blog
	args['months'] = months
	args['category'] = category
	args['tag'] = tag
	args['info'] = info
	args['rec_post'] = rec_post
	return render(request, templa_name, args)

def month_post(request, mp, templa_name="media.html"):
	m_p = mp.encode("utf-8")
	m_p = m_p.split('-')
	info = Data4.objects.all()
	blog = Blog.objects.order_by('title','-posted')
	date_post = Blog.objects.filter(posted__month = m_p[1])
	months = Blog.objects.order_by('posted').distinct('posted')
	print months
	category = Category.objects.order_by('title')
	tag = []
	for i in blog:
		tag = tag + i.tags.split(', ')
	tag = map(str, tag)
	tag = sorted(set(tag))
	args = {}
	args.update(csrf(request))
	args['blog'] = blog
	args['months'] = months
	args['category'] = category
	args['tag'] = tag
	args['info'] = info
	args['date_post'] = date_post
	return render(request, templa_name, args)

def category_post(request, cp, templa_name="media.html"):
	c_p = Category.objects.get(slug = cp)
	cat_post = Blog.objects.filter(category = c_p).order_by('category')
	info = Data4.objects.all()
	blog = Blog.objects.order_by('title','-posted')
	months = Blog.objects.order_by('posted').distinct('posted')
	category = Category.objects.order_by('title')
	tag = []
	for i in blog:
		tag = tag + i.tags.split(', ')
	tag = map(str, tag)
	tag = sorted(set(tag))
	args = {}
	args.update(csrf(request))
	args['blog'] = blog
	args['months'] = months
	args['category'] = category
	args['tag'] = tag
	args['info'] = info
	args['cat_post'] = cat_post
	return render(request, templa_name, args)

def tag_post(request, tp, templa_name="media.html"):
	tag_post = []
	info = Data4.objects.all()
	blog = Blog.objects.order_by('title','-posted')
	months = Blog.objects.order_by('posted').distinct('posted')
	category = Category.objects.order_by('title')
	tag = []
	for i in blog:
		tag = tag + i.tags.split(', ')
		if tp in tag:
			tag_post = tag_post + [i]
	tag = map(str, tag)
	tag = sorted(set(tag))
	args = {}
	args.update(csrf(request))
	args['blog'] = blog
	args['months'] = months
	args['category'] = category
	args['tag'] = tag
	args['info'] = info
	args['tag_post'] = tag_post
	return render(request, templa_name, args)

def jobs(request, templa_name = 'jobs.html'):
	jobs = Jobs.objects.all()
	return render(request, templa_name, locals())
	
def contact(request, templa_name = 'contact.html'):
 	return render(request, templa_name, locals())