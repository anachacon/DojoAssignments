# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import connection

# Create your models here.

class UserManager(models.Manager):
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

    def validate_login(self, request_data):
        valid = True
        email = request_data['email']
        password = request_data['password']
        errors = []
        if email == "":
            errors.append("Please enter email")
            valid = False
        if password == "":
            errors.append("Please enter password")
            valid = False

        if valid == False:
            return valid, errors

        try:
            user = User.objects.get(email=email)
            if password != user.password:
                errors.append("Wrong password")
                valid = False
        except:
            valid = False
            errors.append('User does not exist.')
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

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author= models.ForeignKey(Author, related_name="books")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ReviewManager(models.Manager):
    def last_three(self):
        cursor = connection.cursor()
        cursor.execute('SELECT beltreview_review.id, beltreview_author.name AS author_name, beltreview_book.name AS book_name, beltreview_book.id AS book_id, beltreview_review.desc AS review, beltreview_review.rating, strftime("%m/%d/%Y", beltreview_review.created_at) as date, beltreview_user.name AS user, beltreview_user.id AS user_id FROM beltreview_review JOIN beltreview_book ON beltreview_book.id = beltreview_review.book_id JOIN beltreview_author ON beltreview_book.author_id = beltreview_author.id JOIN beltreview_user ON beltreview_review.user_id = beltreview_user.id ORDER BY beltreview_review.id DESC LIMIT 3')
        reviews = Review.objects.dictfetchall(cursor)
        exclude_books= []
        for review in reviews:
            exclude_books.append(review['book_name'])
        books = Book.objects.exclude(name=exclude_books[0]).exclude(name=exclude_books[1]).exclude(name=exclude_books[2])
        return (reviews, books)

    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def validate_review(self, request_data):
        valid = True
        errors = []
        if request_data['book_title'] == "":
            valid = False
            errors.append('Book title cannot be empty')
        if request_data['review'] == "":
            valid = False
            errors.append('Review cannot be empty')
        if request_data['new_author'] == "" and  request_data['author'] == "0":
            valid = False
            errors.append('Please choose or add author')
        return valid, errors

    def add_review(self, request_data):
        if request_data['new_author'] != "":
            author = Author.objects.create(name = request_data['new_author'])
        else:
            author = Author.objects.get(id=request_data['author'])
        book = Book.objects.create(name = request_data['book_title'], author = author)
        Review.objects.create(book = book, user = User.objects.get(id=request.session['userid']), rating = request_data['rating'], desc = request_data['review'])

class Review(models.Model):
    book= models.ForeignKey(Book, related_name="book_reviews")
    user= models.ForeignKey(User, related_name="user_reviews")
    rating = models.IntegerField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()