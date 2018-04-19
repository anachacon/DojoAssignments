from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import Course
  # the index function is called when root is visited

def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render (request, "courses_app/index.html", context)

def create(request):
    valid = Course.objects.validate_data(request.POST)
    if valid[0] == True:
        Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
        messages.success(request, "You've added a course")
    else: 
        for message in valid[1]:
            messages.error(request, message)
    return redirect ("/")
