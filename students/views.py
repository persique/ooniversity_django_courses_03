# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages


def list_view(request):
    students_course = request.GET
    if 'course_id' in students_course:
        students_on_course = Student.objects.filter(courses=students_course['course_id'])
    else:  
        students_on_course = Student.objects.all()
    return render(request, 'students/list.html', {
			      "students_on_course": students_on_course ,
			       })


def detail(request, students_id):
	students_on_course = Student.objects.filter(pk=students_id)
	return render(request, 'students/detail.html', {
                  'students_on_course': students_on_course
                  })


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u"Student %s %s has been successfully added." % (application.name, application.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm() 
    return render(request, 'students/add.html', {
                  'form': form,
                  })


def edit(request, students_id):
    application = Student.objects.get(id=students_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {
                  'form': form, 
                  })


def remove(request, students_id):
    application = Student.objects.get(id=students_id)
    remove_massage = u"Вы уверены, что хотите удалить студента %s %s ?" % (application.name, application.surname)
    if request.method == 'POST':
        application.delete()
        messages.success(request, u"Info on %s %s has been sucessfully deleted." % (application.name, application.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html',{
                  'remove_massage': remove_massage,
                  })
        



