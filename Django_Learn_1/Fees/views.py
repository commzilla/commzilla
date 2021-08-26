from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_djangof(request):
    return HttpResponse("Hello Django!")

def learn_var(request):
    return HttpResponse("Its a variable")

def learn_math(request):
    a = 50
    return HttpResponse(a)

def learn_format(request):
    a = 'MD RABIUL AWAL SHUVO'
    return HttpResponse(f'Welcome {a}')

def index(request):
    return HttpResponse('Home Page')