from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    a = 'Bangla'
    b = 'English'
    c = 'Math'
    d = 'Biology'
    e = 'Computer Science'
    f = 'Chemistry'
    g = 'Physics'
    return HttpResponse(f'There is some course = {a, b, c, d, e, f, g}')