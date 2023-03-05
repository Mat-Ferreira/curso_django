from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    return HttpResponse("Hello world")


def about(req):
    return HttpResponse("<h1>About me</h1>")


def contact(req):
    return HttpResponse("<h2> Contact info</h2>")
