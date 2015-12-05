from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
import quadratic
import courses

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/' ,include('students.urls')),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
	url(r'^courses/', include('courses.urls')),
]
