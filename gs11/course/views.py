from django.shortcuts import render
from datetime import datetime

# Create your views here.
def bangla(request):
    cname = 'django'
    duration = '4 Month'
    seats = 0
    d = datetime.now()
    number = 48.00000
    number2 = 48.45325
    ban = 'Bangla'
    checker = False
    django_details = {'ck':checker,'ban':ban,'checker':True,'nm':cname,'du':duration,'st':seats, 'dt':d, 'n1':number, 'n2':number2}
    return render(request, 'course/courseone.html',django_details)

def english(request):
    # student = {'names':['Rahul','Sonam','Raj','Anu']}
    data = {'name': 'Rahul', 'roll':101}
    data2 = {'name': 'Anu', 'roll':102}
    return render(request, 'course/coursetwo.html',{'data': data})
