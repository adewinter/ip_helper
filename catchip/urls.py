from django.conf.urls.defaults import *
from ip_helper.catchip import views


urlpatterns = patterns('',
     url(r'^$',views.show_all, name='show-all'),
)