from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    unique_id = get_random_string(length=14)
    context = {
        "word":unique_id
    }
    return render (request, "randomw/index.html", context)

def reset(request):
    del request.session['counter']
    return redirect ("/")