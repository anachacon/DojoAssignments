from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager): #default function .get/.filter/.all/.first
    def validate_data(self, request_data):
        valid = True
        errors = []
        if request_data['name'] == "":
            valid = False
            errors.append('Name cannot be empty')
        if request_data['desc'] == "":
            valid = False
            errors.append('Description cannot be empty')
        if len(request_data['name']) < 5 :
            valid = False
            errors.append('Name has to be more than 5 characters')
        if len(request_data['desc']) < 15:
            valid = False
            errors.append('Description has to be more than 15 characters')
      
        return valid, errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.name