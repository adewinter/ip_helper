from django.conf.urls.defaults import *
from ip_helper.catchip import views


urlpatterns = patterns('',
     url(r'^record/(?P<machine_name>\w+)/', views.record, name='record-ip'),
     url(r'^record/', views.show_all),
     url(r'^$',views.show_all, name='show-all'),
     url(r'^getip/(?P<machine_name>\w+)$', views.get_ip, name='get-ip'),
     url(r'^getip/', views.get_ip),
)