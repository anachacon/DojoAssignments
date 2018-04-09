from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
  # the index function is called when root is visited
def index(request):
  context = {
  "date": strftime("%b %d, %Y", gmtime()),
  "time": strftime("%I:%M %p", gmtime())

  }
  return render(request,'displayt/index.html', context)

