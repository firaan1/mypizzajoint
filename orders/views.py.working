from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.serializers import serialize
import json

from .models import *

# check email function
import re
def check_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def user_cost(object):
    total = 0
    user_id = object.user.id
    for order in OrderPizza.objects.filter(user_id = user_id):
        total += order.pizzachoice.price
    for order in OrderSub.objects.filter(user_id = user_id):
        total += order.subchoice.price
        # total += order.subextra.price
    for order in OrderPasta.objects.filter(user_id = user_id):
        total += order.pastachoice.price
    for order in OrderSalad.objects.filter(user_id = user_id):
        total += order.saladchoice.price
    for order in OrderDinnerPlatter.objects.filter(user_id = user_id):
        total += order.dinnerplatterchoice.price
    return(total)


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    context = {
        "pizzas" : PizzaRate.objects.all()
    }
    # return HttpResponse("Project 3: TODO")
    return render(request, "orders/index.html", context)

@login_required(login_url='/login')
def order(request):
    total_cost = user_cost(request)
    pizzatype,pizzasize,toppingtype = {},{},{}
    for p in PizzaRate.objects.all():
        pizzatype[p.pizzatype_id] = str(p.pizzatype)
        pizzasize[p.pizzasize_id] = str(p.pizzasize)
        toppingtype[p.toppingtype_id] = str(p.toppingtype)
    toppingchoice = {}
    for t in ToppingChoice.objects.all():
        toppingchoice[t.pk] = str(t)
    context = {
    "total_cost": total_cost,
    "pizzatype": json.dumps(pizzatype),
    "pizzasize": json.dumps(pizzasize),
    "toppingtype": json.dumps(toppingtype),
    "toppingchoice": json.dumps(toppingchoice),
    "pizzarate": serialize("json",PizzaRate.objects.all())
    }
    return render(request, "orders/order.html", context)

@login_required(login_url="/login")
def change_order(request):
    if request.method == "POST":
        menutype = str(request.POST['menutype'])
        rate_pk = str(request.POST['rate_pk'])
        quantity = int(request.POST['quantity'])
        others = str(request.POST['others'])
        if others == "":
            others = []
        else:
            others = others.split(",")
        user_object = User.objects.get(pk = request.user.pk)
        response = {}
        if menutype == "pizza":
            for q in range(0,quantity):
                pizzarate_object = PizzaRate.objects.get(pk = rate_pk)
                orderpizza = OrderPizza(user = user_object, pizzachoice = pizzarate_object)
                orderpizza.save()
                if others:
                    toppingchoice_object = [ToppingChoice.objects.get(pk = o) for o in others]
                    orderpizza.toppingchoice.set(toppingchoice_object)
                    orderpizza.save()
                response[orderpizza.pk] = {
                "menutype" : "pizza",
                "main" : str(orderpizza.pizzachoice),
                "others" : json.loads(serialize("json",orderpizza.toppingchoice.all()))
                }
                del(orderpizza)
        return HttpResponse(json.dumps(response))

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message" : None})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message" : "Invalid credentials"})

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", { "message" : "Logged out successfully"})

def register_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "orders/login.html", {"message" : "User already logged in"})
        else:
            return render(request, "orders/register.html", {"message" : None})
    else:
        username = request.POST["username"]
        useremail = request.POST["useremail"]
        password = request.POST["password"]
        password_retype = request.POST["password_retype"]
        userlist = [u.username for u in User.objects.all()]
        if username in userlist:
            return render(request, "orders/register.html", {"message" : "User already exist"})
        if password == password_retype and check_email(useremail):
            try:
                user = User.objects.create_user(username, useremail, password)
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            except:
                return render(request, "orders/register.html", {"message" : "Error in user registration"})
        else:
            return render(request, "orders/register.html", {"message" : "Check user credentials"})
