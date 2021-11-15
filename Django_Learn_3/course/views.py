from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Learn_django(request):
    return HttpResponse("Hello Learn_Django")

def Learn_python(request):
    return HttpResponse("Hello Learn_Python")