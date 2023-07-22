from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>fisrt response of app2</h1>')

def second(request):
    return HttpResponse('<h1>second response of app2</h1>')


# Create your views here.
