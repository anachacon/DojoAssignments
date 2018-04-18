from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager): #default function .get/.filter/.all/.first
    def validate_data(self, request_data):
        valid = True
        errors = []
        if request_data['first_name'] == "":
            valid = False
            errors.append('First name cannot be empty')
        if request_data['last_name'] == "":
            valid = False
            errors.append('Last name cannot be empty')
        if request_data['email'] == "":
            valid = False
            errors.append('Email cannot be empty')
        return valid, errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name
