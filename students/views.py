# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages


def list_view(request):
    get_course_id = request.GET.get('course_id', None)

    courses_list = Course.objects.all()

    if get_course_id:

        students_list = Student.objects.filter(courses=Course.objects.get(id=get_course_id))

    else:

        students_list = Student.objects.all()

    return render(request, 'students/list.html', {'students_list': students_list, 'courses_list': courses_list})


def detail(request, student_id):
    student_details = Student.objects.get(id=student_id)

    return render(request, 'students/detail.html', {'student_details': student_details})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form_content = form.cleaned_data
            form.save()
            notification = u"Студент %s %s успешно добавлен" % (form_content['name'].encode('utf-8'), form_content['surname'].encode('utf-8'))
            messages.success(request, notification)
        return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, u"Данные изменены")
            return render(request, 'students/edit.html', {'form': form})

    form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})
