from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import connection
from models import *
# the index function is called when root is visited
def index(request):
    return render(request, "beltreview/index.html")

def register(request):
    if 'userid' in request.session:
        return redirect ("/books")
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
    cursor = connection.cursor()
    cursor.execute('SELECT beltreview_author.name AS author_name, beltreview_book.name AS book_name, beltreview_review.desc AS review, beltreview_review.rating, beltreview_user.name AS user, beltreview_user.id AS user_id FROM beltreview_review JOIN beltreview_book ON beltreview_book.id = beltreview_review.book_id JOIN beltreview_author ON beltreview_book.author_id = beltreview_author.id JOIN beltreview_user ON beltreview_review.user_id = beltreview_user.id')
    reviews = dictfetchall(cursor)
    context = {
        "user": user,
        "reviews" : reviews
    }
    return render(request, "beltreview/books.html", context)

def logout(request):
    del request.session['userid']
    return redirect ("/")

def add(request):
    pass

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

