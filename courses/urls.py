from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
    url(r'(?P<request_id>[0-9]+)/$', views.detail, name = "detail")
)
