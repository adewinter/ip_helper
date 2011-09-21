from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from ip_helper.catchip.views import show_all
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', show_all, name='dashboard'),
    url(r'^catchip/$', include('ip_helper.catchip.urls')),
    # url(r'^ip_helper/', include('ip_helper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
