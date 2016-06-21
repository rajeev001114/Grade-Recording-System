from django.conf.urls import patterns, url
from LGN import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='login'),
	url(r'^validatelogin/$', views.validatelogin, name='validatelogin'),
)

