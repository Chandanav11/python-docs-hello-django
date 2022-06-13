from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Chandana, Good Morning! We are learning Azure and we are Happy")
