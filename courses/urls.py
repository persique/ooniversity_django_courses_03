from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import detail, create, edit, remove, add_lesson

urlpatterns = patterns('',
                       # url(r'^$', pybursa.views.index, name="index")
                       url(r'^(?P<course_id>\d+)/$', detail, name="detail"),
                       url(r'^add/$', create, name="add"),
                       url(r'^edit/(?P<course_id>\d+)/$', edit, name="edit"),
                       url(r'^remove/(?P<course_id>\d+)/$', remove, name="remove"),
                       url(r'^(?P<course_id>\d+)/add_lesson$', add_lesson, name="add-lesson"),
                       )
