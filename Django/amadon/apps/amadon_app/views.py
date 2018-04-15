from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    request.session['prices']={"1":"19.99","2":"29.99","3":"4.99","4":"49.99"}
    return render(request, "amadon_app/index.html")
 
def buy(request):
    p_id = request.POST['product_id']
    quant = int(request.POST['quantity'])
    price = float(request.session['prices'].get(p_id))
    if 'counter' not in request.session:
        request.session['counter'] = quant
    else:
        request.session['counter'] += quant
    if 'total' not in request.session:
        request.session['total'] = quant * price
    else:
        request.session['total'] += quant * price
    request.session['charge'] = quant * price
    return redirect("/checkout")

def checkout(request):
    context = {
        "charge" : request.session['charge'],
        "total" : request.session['total'],
        "counter" : request.session['counter']
    }
    return render(request, "amadon_app/checkout.html", context)

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect("/")