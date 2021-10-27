from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! <br/> <a href='/parasitologyTool/about/'>About</a>.")

def about(request):
    return HttpResponse("about page")