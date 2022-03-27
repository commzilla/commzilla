from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fee_django(request):
    return HttpResponse("<h1>Hello Django! fee</h1>")

def fee_python(request):
    return HttpResponse("<h1>Hello Python fee</h1>")