from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views


urlpatterns = patterns('',
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^add/$', views.create, name='create'),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove, name='remove'),
)



