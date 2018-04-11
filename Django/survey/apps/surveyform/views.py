from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  return render(request, "surveyform/index.html")

def process(request):
  if(not 'counter' in request.session):
    request.session['counter']=1
  else:
    request.session['counter'] = request.session['counter'] + 1
  request.session['name'] = request.POST['name']
  request.session['location'] = request.POST['location']
  request.session['language'] = request.POST['language']
  if len(request.POST['comment']) > 0:
    request.session['comment'] = request.POST['comment']
  else:
   request.session['comment'] =  "No comment"
  return redirect ("/result")


def result(request):
  return render (request, "surveyform/result.html")
    
def reset(request):
  for key in request.session.keys():
    del request.session[key]
  return redirect ("/")