# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager): #default function .get/.filter/.all/.first
    def validate_data(self, request_data):
        valid = True
        errors = []
        if request_data['name'] == "":
            valid = False
            errors.append('Name cannot be empty')
        if request_data['alias'] == "":
            valid = False
            errors.append('Alias cannot be empty')
        if request_data['email'] == "":
            valid = False
            errors.append('Email cannot be empty')
        if request_data['password'] == "":
            valid = False
            errors.append('Password cannot be empty')
        if len(request_data['password']) < 8:
            valid = False
            errors.append('Password must be at least 8 characters.')
        if request_data['password_confirm'] == "":
            valid = False
            errors.append('Please confirm password')
        if request_data['password_confirm'] != request_data['password']:
            valid = False
            errors.append('Passwords do not match')
        return valid, errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.name