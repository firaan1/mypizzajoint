from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    context = {
    "user" : request.user
    }
    return HttpResponse("Project 3: TODO")
