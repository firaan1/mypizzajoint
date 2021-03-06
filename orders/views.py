from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.serializers import serialize
import json
import stripe
import datetime

from .models import *

# check email function
import re
def check_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def user_cost(object):
    total_cost = 0
    order_list = []
    user_id = object.user.id
    for order in OrderPizza.objects.filter(user_id = user_id, paid = False):
        total_cost += order.pizzachoice.price
        order_list.append(order)
    for order in OrderSub.objects.filter(user_id = user_id, paid = False):
        total_cost += order.subchoice.price
        for o in order.subextrachoice.all():
            total_cost += o.price
        order_list.append(order)
        # total_cost += order.subextra.price
    for order in OrderPasta.objects.filter(user_id = user_id, paid = False):
        total_cost += order.pastachoice.price
        order_list.append(order)
    for order in OrderSalad.objects.filter(user_id = user_id, paid = False):
        total_cost += order.saladchoice.price
        order_list.append(order)
    for order in OrderDinnerPlatter.objects.filter(user_id = user_id, paid = False):
        total_cost += order.dinnerplatterchoice.price
        order_list.append(order)
    return dict(order_list = order_list, total_cost = total_cost)

def add_paid_orders(object, address_to_delivery):
    last_orders = user_cost(object)
    placed_order = PlacedOrder(user = object.user, deliveryaddress = DeliveryAddress.objects.get(pk = address_to_delivery))
    placed_order.save()
    pizzas = [s for s in OrderPizza.objects.filter(user = object.user, paid = False)]
    subs = [s for s in OrderSub.objects.filter(user = object.user, paid = False)]
    pastas = [s for s in OrderPasta.objects.filter(user = object.user, paid = False)]
    salads = [s for s in OrderSalad.objects.filter(user = object.user, paid = False)]
    dinnerplatters = [s for s in OrderDinnerPlatter.objects.filter(user = object.user, paid = False)]
    try:
        placed_order.orderpizza.set(pizzas)
        placed_order.ordersub.set(subs)
        placed_order.orderpasta.set(pastas)
        placed_order.ordersalad.set(salads)
        placed_order.orderdinnerplatter.set(dinnerplatters)
        placed_order.save()
        for order in pizzas + subs + pastas + salads + dinnerplatters:
            order.paid = True
            order.save()
        placed_order.totalprice = last_orders['total_cost']
        placed_order.save()
        placed_order.datetime = datetime.datetime.now()
        placed_order.save()
        return "done"
    except Exception as e:
        return e

menu_dict = {"pizza" : OrderPizza, "sub" : OrderSub, "pasta" : OrderPasta, "salad" : OrderSalad, "dinnerplatter" : OrderDinnerPlatter, "pizzarate" : PizzaRate, "subrate" : SubRate, "pastarate" : PastaRate, "saladrate" : SaladRate, "dinnerplatterrate" : DinnerPlatterRate}

def delete_order(menutype, pk):
    request_order = menu_dict[menutype].objects.get(pk = pk)
    request_order.delete()

def add_order(menutype, pk, others, quantity, user):
    for q in range(0,int(quantity)):
        request_order = menu_dict[f"{menutype}rate"].objects.get(pk = pk)
        if menutype == "pizza":
            place_order = menu_dict[menutype](user = user, pizzachoice = request_order)
        elif menutype == "sub":
            place_order = menu_dict[menutype](user = user, subchoice = request_order)
        elif menutype == "pasta":
            place_order = menu_dict[menutype](user = user, pastachoice = request_order)
        elif menutype == "salad":
            place_order = menu_dict[menutype](user = user, saladchoice = request_order)
        elif menutype == "dinnerplatter":
            place_order = menu_dict[menutype](user = user, dinnerplatterchoice = request_order)
        place_order.save()
        if others:
            if menutype == "pizza":
                toppingchoice = [ToppingChoice.objects.get(pk = o) for o in others]
                place_order.toppingchoice.set(toppingchoice)
            if menutype == "sub":
                subextrachoice = [SubExtraRate.objects.get(pk = o) for o in others]
                place_order.subextrachoice.set(subextrachoice)
            place_order.save()



# Create your views here.
def index(request):
    context = {
        "pizzas" : PizzaRate.objects.all(),


            "pizzatype" : PizzaRate.pizzatype.get_queryset(),
            "pizzasize" : PizzaRate.pizzasize.get_queryset(),
            "toppingtype" : PizzaRate.toppingtype.get_queryset(),
            "toppingchoice" : ToppingChoice.objects.all(),
            "pizzarate" : PizzaRate.objects.all(),

            "subchoice" :  SubRate.subchoice.get_queryset(),
            "subsize" :  SubRate.subsize.get_queryset(),
            "subextrachoice" :  SubExtraRate.objects.all(),
            "subrate" :  SubRate.objects.all(),

            "pastarate" :  PastaRate.objects.all(),

            "saladrate" :  SaladRate.objects.all(),

            "dinnerplatterrate" :  DinnerPlatterRate.objects.all(),
            "dinnerplattersize" :  DinnerPlatterRate.dinnerplattersize.get_queryset(),
            "dinnerplatterchoice" :  DinnerPlatterRate.dinnerplatterchoice.get_queryset()
    }
    return render(request, "orders/index.html", context)

@login_required(login_url='/login')
def show_order(request):
    if request.method == "POST":
        todo = request.POST['todo']
        if todo == "address":
            new_address = request.POST['new_address']
            new_number = request.POST['new_number']
            address = DeliveryAddress(user = request.user, address = new_address, phone_number = new_number)
            address.save()
        elif todo == "deleteaddress":
            address_pk = request.POST['address_pk']
            delete_address = DeliveryAddress.objects.filter(user = request.user, pk = address_pk).last()
            if delete_address:
                delete_address.delete()
    last_orders = user_cost(request)
    context = {
    "last_orders" : last_orders,
    "user_email" : request.user.email,
    "deliveryaddress" : DeliveryAddress.objects.filter(user = request.user).order_by('-pk')
    }
    return render(request, "orders/show_order.html", context)

@login_required(login_url='/login')
def make_payment(request):
    status = None
    if request.method == "POST":
        stripe.api_key = "sk_test_tSFhKEyCfNka1V4A71VZWbWc"
        token = request.POST['stripeToken']
        amount = request.POST['amount']
        address_to_delivery = request.POST['address_to_delivery']
        try:
            charge = stripe.Charge.create( amount=int(amount), currency='usd', description='charge', source=token)
            status = "success"
            test = add_paid_orders(request, address_to_delivery);
        except Exception as e:
            status = str(e)
    if not status:
        status = "get"
    paid_orders = PlacedOrder.objects.filter(user = request.user)
    context = {
    "paid_orders" : paid_orders,
    "status" : status,
    }
    return render(request, "orders/make_payment.html", context)

@login_required(login_url='/login')
def order(request):
    last_orders = user_cost(request)
    context = {
    "last_orders" : last_orders,

    "pizzatype" : serialize("json",PizzaRate.pizzatype.get_queryset()),
    "pizzasize" : serialize("json",PizzaRate.pizzasize.get_queryset()),
    "toppingtype" : serialize("json",PizzaRate.toppingtype.get_queryset()),
    "toppingchoice" : serialize("json",ToppingChoice.objects.all()),
    "pizzarate" : serialize("json",PizzaRate.objects.all()),

    "subchoice" : serialize("json", SubRate.subchoice.get_queryset()),
    "subsize" : serialize("json", SubRate.subsize.get_queryset()),
    "subextrachoice" : serialize("json", SubExtraRate.objects.all()),
    "subrate" : serialize("json", SubRate.objects.all()),

    "pastarate" : serialize("json", PastaRate.objects.all()),

    "saladrate" : serialize("json", SaladRate.objects.all()),

    "dinnerplatterrate" : serialize("json", DinnerPlatterRate.objects.all()),
    "dinnerplattersize" : serialize("json", DinnerPlatterRate.dinnerplattersize.get_queryset()),
    "dinnerplatterchoice" : serialize("json", DinnerPlatterRate.dinnerplatterchoice.get_queryset())
    }
    return render(request, "orders/order.html", context)

@login_required(login_url="/login")
def change_order(request):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('index'))
    user = request.user
    menutype = request.POST['menutype']
    pk = request.POST['pk']
    todo = request.POST['todo']
    if todo == "delete":
        delete_order(menutype, pk)
    elif todo == "add":
        quantity = request.POST['quantity']
        others = request.POST['others']
        if others == "":
            others = []
        else:
            others = others.split(",")
        add_order(menutype, pk, others, quantity, user)
    return HttpResponse(todo)


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
