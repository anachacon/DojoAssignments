from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User
# the index function is called when root is visited
def index(request):
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

def books(request):
    response = ("Welcome user num: {}".format(request.session['userid']))
    return HttpResponse(response)

def login(request):
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)
    except:
        messages.error(request, "User does not exist")
        return redirect ("/")
    if request.POST['password'] != user.password:
        messages.error(request, "Wrong password")
        return redirect ("/")
    request.session['userid'] = user.id
    return redirect ("/books")