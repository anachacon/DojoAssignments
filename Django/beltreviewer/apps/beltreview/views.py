from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from django.db import connection
from models import *
# the index function is called when root is visited
def index(request):
    if 'userid' in request.session:
        return redirect ("/books")
    return render(request, "beltreview/index.html")

def register(request):  
    valid = User.objects.validate_data(request.POST)
    if valid[0] == True:
        user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'])
        request.session['userid'] = user.id
        return redirect ("/books")
    else: 
        for message in valid[1]:
            messages.error(request, message)
        return redirect ("/")

def login(request):
    valid = User.objects.validate_login(request.POST)
    if valid[0] == True:
        user = User.objects.get(email = request.POST['email'])
        request.session['userid'] = user.id
        return redirect ("/books")
    else: 
        for message in valid[1]:
            messages.error(request, message)
        return redirect ("/")

def books(request):
    user = User.objects.get(id = request.session['userid'])
    reviews_books = Review.objects.last_three()
    context = {
        "user": user,
        "reviews" : reviews_books[0],
        "books" : reviews_books[1]
    }
    return render(request, "beltreview/books.html", context)

def logout(request):
    del request.session['userid']
    return redirect ("/")

def add(request):
    authors = Author.objects.all()
    context = {
        "authors" : authors
    }
    return render(request, "beltreview/add.html", context)

def book_add(request):
    valid = Review.objects.validate_review(request.POST)
    if valid[0] == True:
        book_id = Review.objects.add_review(request.POST, request.session['userid'])
        return redirect ("/books/{}".format(book_id))
    else: 
        for message in valid[1]:
            messages.error(request, message)
        return redirect ("/books/add")

def book(request, id):
    book = Book.objects.get(id=id)
    reviews = Review.objects.filter(book = book)
    context = {
        "book" : book,
        "reviews" : reviews,
        "user_id" : request.session['userid']
    }
    return render(request, "beltreview/book.html", context)

def review_add(request):
    book = Book.objects.get(id = request.POST['book'])
    user = User.objects.get(id = request.session['userid'])
    rating = request.POST['rating']
    desc = request.POST['review']
    review = Review.objects.create(book = book, user = user, rating = rating, desc = desc)
    return redirect ("/books/{}".format(book.id))

def user(request, id):
    user = User.objects.get(id=id)
    books = Review.objects.books(id)
    total_reviews = len(books)
    context = {
        "user" : user,
        "books" : books,
        "total_reviews" : total_reviews
    }
    return render(request, "beltreview/user.html", context)

def delete(request, id):
    book_id = Review.objects.get(id=id).book_id
    Review.objects.get(id=id).delete()
    return redirect ("/books/{}".format(book_id))