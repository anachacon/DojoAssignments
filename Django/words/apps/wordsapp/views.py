from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, "wordsapp/index.html")

def process(request):
    if 'words' not in request.session:
        request.session['words'] = []
    word = request.POST['word']
    color = request.POST['color']
    if 'size' in request.POST:
        color += " big"
    time = strftime("%I:%M %p , %b %d %Y", gmtime())
    new_word = {"word":word, "wclass":color, "time":time}
    request.session['words'].append(new_word)
    request.session.modified = True
    return redirect("/")

def clear(request):
    del request.session['words']
    return redirect ("/")
