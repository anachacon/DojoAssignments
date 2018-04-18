from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User
# the index function is called when root is visited

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, "users/new.html")

def edit(request, id):
    edit_user = User.objects.get(id=id)
    context = {
        "id":edit_user.id,
        "first_name": edit_user.first_name,
        "last_name": edit_user.last_name,
        "email": edit_user.email
    }
    return render(request, "users/edit.html", context)

def show(request, id):
    show_user = User.objects.get(id=id)
    context = {
        "id":show_user.id,
        "first_name": show_user.first_name,
        "last_name": show_user.last_name,
        "email": show_user.email,
        "date": show_user.created_at
    }
    return render(request, "users/show.html", context)

def destroy(request, id):
    User.objects.filter(id=id).delete()
    return redirect ("/users")

def create(request):
    valid = User.objects.validate_data(request.POST)
    if valid[0] == True:
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        messages.success(request, 'You created a user!')
    else: 
        for message in valid[1]:
            messages.error(request, message)
    return redirect ("/users")

def update(request):
    user_id = request.POST['user_id']
    valid = User.objects.validate_data(request.POST)
    if valid[0] == True:
        User.objects.filter(id=user_id).update(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        return redirect ("/users")
    else: 
        for message in valid[1]:
            messages.error(request, message)
        url = "{}/edit".format(user_id)
        return redirect (url)
   
