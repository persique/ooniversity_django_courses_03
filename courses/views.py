# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

class CourseDetailView(DetailView):
	model = Course
	template_name = "courses/detail.html"
	context_object_name = "course"

"""
def detail(request, course_id):
	#course = Course.objects.get(id=course_id)
	course = get_object_or_404(Course, id=course_id)
	return render(request, 'courses/detail.html', {'course':course})
"""


class CourseCreateView(CreateView):
	model = Course
	template_name = "courses/add.html"
	success_url = reverse_lazy('index')
	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = "Course creation"
		#context['page_title'] = "Student registration"
		return context
	def form_valid(self, form):
		cour = form.save()
		mes = "Course %s has been successfully added." % cour.name
		messages.success(self.request, mes)
		return super(CourseCreateView, self).form_valid(form)

"""
def create(request):
	if request.method == "POST":
		form = CourseModelForm(request.POST)
		if form.is_valid():
			cour = form.save()
			mes = u'Course %s has been successfully added.' % cour.name
			messages.success(request, mes)
			return redirect("/")
	else:
		form = CourseModelForm()
	return render(request, "courses/add.html", {'form':form})
"""

class CourseUpdateView(UpdateView):
	model = Course
	template_name = "courses/edit.html"
	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Course update"
		#context['page_title'] = "Student registration"
		return context
	def form_valid(self, form):
		mes = "The changes have been saved."
		messages.success(self.request, mes)
		self.success_url = reverse_lazy('courses:edit', kwargs = {'pk':self.object.pk})
		return super(CourseUpdateView, self).form_valid(form)
	

"""
def edit(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		form = CourseModelForm(request.POST, instance=course)
		if form.is_valid():
			cour = form.save()
			mes = u'The changes have been saved.'
			messages.success(request, mes)
			return redirect('courses:edit',  cour.id)
	else:
		form = CourseModelForm(instance=course)
	return render(request, "courses/edit.html", {'form':form})
"""

class CourseDeleteView(DeleteView):
	model = Course
	template_name = "courses/remove.html"
	success_url = reverse_lazy('index')
	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Course deletion"
		mes = "Course %s has been deleted." % self.object.name
		messages.success(self.request, mes)
		#context['page_title'] = "Student registration"
		return context
"""
def remove(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		course.delete()
		mes = u'Course %s has been deleted.' % course.name
		messages.success(request, mes)
		return redirect("/")

	return render(request, "courses/remove.html", {'name':course.name})
"""	

class LessonCreateView(CreateView):
	model = Lesson
	template_name = "courses/add_lesson.html"
	def form_valid(self, form):
		les = form.save()
		mes = "Lesson %s has been successfully added." % les.subject
		messages.success(self.request, mes)
		return super(LessonCreateView, self).form_valid(form)
	def get_success_url(self):
		return reverse_lazy('courses:detail', kwargs = {'pk':self.object.course.pk})

"""
def add_lesson(request, course_id):
	if request.method == "POST":
		form = LessonModelForm(request.POST)
		if form.is_valid():
			les = form.save()
			mes = u'Lesson %s has been successfully added.' % les.subject
			messages.success(request, mes)
			return redirect('courses:detail', les.course.id)
	else:
		form = LessonModelForm()
	return render(request, "courses/add_lesson.html", {'form':form})
"""
