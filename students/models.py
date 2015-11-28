from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=90)
    phone = models.CharField(default='80-80-80', max_length=30)
    short_description = models.CharField(max_length=100)
    skype = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)
