from django.contrib import admin
from D4_Website.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class Data4Admin(admin.ModelAdmin):
	list_display = ['about', 'what_we_do', 'story', 'manifesto', 'team']
	search_fields = ['about', 'what_we_do', 'story', 'manifesto', 'team']
admin.site.register(Data4, Data4Admin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class MyUserAdmin(UserAdmin):
	list_display = ['username', 'email', 'first_name', 'last_name', 'email', 'is_staff', 'last_login']
	inlines = [UserProfileInline, ]

try:
	admin.site.unregister(User)
finally:
	admin.site.register(User, MyUserAdmin)

class JobsAdmin(admin.ModelAdmin):
	list_display = ['title', 'posted', 'area', 'english_level', 'relocation', 'formalities', 'description', 'requeriments', 'salary', 'to_begin_in', 'contract_type', 'contact', 'phone', 'email']
	search_fields = ['title', 'posted', 'area', 'english_level', 'relocation', 'salary', 'to_begin_in', 'contract_type', 'contact', 'phone', 'email']
admin.site.register(Jobs, JobsAdmin)

class ClientsAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'company_RP', 'company_website', 'company_address', 'company_country', 'company_associated_date']
	search_fields = ['company_name', 'company_RP', 'company_country', 'company_associated_date']
admin.site.register(Clients, ClientsAdmin)

class ProjectsAdmin(admin.ModelAdmin):
	list_display = ['project_name', 'description', 'mandated', 'get_members', 'start_date', 'finish_date', 'company']
	search_fields = ['project_name', 'mandated', 'company']
admin.site.register(Projects, ProjectsAdmin)

class BlogAdmin(admin.ModelAdmin):
	exclude = ['posted']
	list_display = ['title', 'get_creator', 'body', 'category', 'slug', 'image']
	search_fields = ['title', 'body', 'category', 'posted']
	prepopulated_fields = {'slug': ('title',)}
admin.site.register(Blog, BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class SnapShootsAdmin(admin.ModelAdmin):
	list_display = ['project']
	search_fields = ['project']
admin.site.register(SnapShoots, SnapShootsAdmin)