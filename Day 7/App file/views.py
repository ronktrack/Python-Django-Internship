from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepageview(request):
    return HttpResponse("<h1><b>Hello Jevin to your first site</b></h1>")

def aboutpageview(request):
    return HttpResponse("<h1>About</h1>")

def contactpageview(request):
    return HttpResponse("<h1>9265013575</h1>")