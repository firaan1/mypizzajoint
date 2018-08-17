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
    # pizzatype = list(set([(x.pizzatype_id, str(x.pizzatype)) for x in PizzaRate.objects.all()]))
    # pizzasize = list(set([(x.pizzasize_id, str(x.pizzasize)) for x in PizzaRate.objects.all()]))
    # toppingtype = list(set([(x.toppingtype_id, str(x.toppingtype)) for x in PizzaRate.objects.all()]))
    # toppingchoice = list([(t.pk,t.toppingchoice) for t in ToppingChoice.objects.all()])
    pizzatype,pizzasize,toppingtype = {},{},{}
    for p in PizzaRate.objects.all():
        pizzatype[p.pizzatype_id] = str(p.pizzatype)
        pizzasize[p.pizzasize_id] = str(p.pizzasize)
        toppingtype[p.toppingtype_id] = str(p.toppingtype)
    toppingchoice = {}
    for t in ToppingChoice.objects.all():
        toppingchoice[t.pk] = str(t)
    context = {
    "pizzatype": json.dumps(pizzatype),
    "pizzasize": json.dumps(pizzasize),
    "toppingtype": json.dumps(toppingtype),
    "toppingchoice": json.dumps(toppingchoice),
    "pizzarate": PizzaRate.objects.all()
    }
    return render(request, "orders/order.html", context)

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
