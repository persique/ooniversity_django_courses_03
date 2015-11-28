# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Course, Lesson


def list_view(request):
    list_courses = Course.objects.all().order_by('name')
    context = {
        'list_courses': list_courses,
    }
    return render_to_response('courses/list_courses.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
    }
    return render_to_response('courses/detail.html', context)
