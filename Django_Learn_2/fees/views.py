from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fee(request):
    a = 100
    b = 200
    c = 300
    d = 300
    e = 300
    f = 300
    g = 500
    return HttpResponse(f'There is some course fee = {a, b, c, d, e, f, g}')