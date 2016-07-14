from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'D4_Website.views.home', name='home'),
    #url(r'^$', 'D4_Website.views.main', name='main'),
    url(r'^home$', 'D4_Website.views.main', name='main'),
    url(r'^us$', 'D4_Website.views.us', name='us'),
    url(r'^work$', 'D4_Website.views.work', name='work'),
    url(r'^work/category_job/(?P<cj>\S+)$', 'D4_Website.views.category_job', name='category_job'),
    url(r'^media$', 'D4_Website.views.media', name='media'),
    url(r'^media/search_post$', 'D4_Website.views.search_post', name='search_post'),
    url(r'^media/recent_post/(?P<rp>\S+)$', 'D4_Website.views.recent_post', name='recent_post'),
    url(r'^media/month_post/(?P<mp>\S+)$', 'D4_Website.views.month_post', name='month_post'),
    url(r'^media/category_post/(?P<cp>\S+)$', 'D4_Website.views.category_post', name='category_post'),
    url(r'^media/tag_post/(?P<tp>\S+)$', 'D4_Website.views.tag_post', name='tag_post'),
    url(r'^jobs/$', 'D4_Website.views.jobs', name='jobs'),
    url(r'^contact/$', 'D4_Website.views.contact', name='contact'),

    url(r'^isotope$', 'D4_Website.views.isotope', name='isotope'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
