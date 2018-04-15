from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime as dt
import random

def index(request):
    if 'gold' not in request.session:
            request.session['gold'] = 0
            request.session['activity'] = []
    context = {
        "gold" : request.session['gold'],
        "activities" : request.session['activity']
    }
    return render (request, "ninja/index.html", context)

def process(request):
    activity = request.session['activity']
    time = dt.strftime(dt.now(), "%Y/%m/%d, %I:%M %p")

    if request.POST["building"] == "farm":
        winnings = random.randrange(10, 21)
        request.session['gold'] = request.session['gold'] + winnings
        activity.append({
            "message": "Earned {} golds from the farm! ({})".format(winnings, time),
            "color":"green"
        })

    if request.POST["building"] == "cave":
        winnings = random.randrange(5, 11)
        request.session['gold'] = request.session['gold'] + winnings
        activity.append({
            "message": "Earned {} golds from the cave! ({})".format(winnings, time),
            "color":"green"
        })

    if request.POST["building"] == "house":
        winnings = random.randrange(2, 6)
        request.session['gold'] = request.session['gold'] + winnings
        activity.append({
            "message": "Earned {} golds from the house! ({})".format(winnings, time),
            "color":"green"
        })

    if request.POST["building"] == "casino":
        game = random.randrange(0, 2)
        winnings = random.randrange(0, 51)
        if game == 0:
            request.session['gold'] = request.session['gold'] - winnings
            activity.append({
            "message": "Entered a casino and lost {} golds... Ouch ({})".format(winnings, time),
            "color": "red"
             })
        else: 
            request.session['gold'] = request.session['gold'] + winnings
            activity.append({
            "message": "Entered a casino and won {} golds! ({})".format(winnings, time),
            "color": "green"
             })

    request.session.modified = True
    return redirect('/')

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect("/")