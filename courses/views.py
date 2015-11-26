from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson
from django.core.exceptions import ObjectDoesNotExist

def detail(request, pk):
    try:
        courses = get_object_or_404(Course, id = pk)
        lessons = courses.lesson_set.all()
        return render(request, 'courses/detail.html', { 
                      'courses':courses , 
                      'lessons':lessons, 
                      })
    except ObjectDoesNotExist:
        achtung = "Houston, we have a problem with id = {0} exist yet.".format(pk) 
	return render(request, 'courses/detail.html', {
		    "achtung": achtung,
            })

            
