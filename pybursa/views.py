from django.shortcuts import render
from courses.models import Course
import logging

logger = logging.getLogger(__name__)

def index(request):
	logger.debug("Debug - logger!")
	logger.info("INFO - logger!")
	logger.error("ERROR - logger!")
	return render(request, 'index.html', {'courses':Course.objects.all()})

#def index(request):
#	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')


