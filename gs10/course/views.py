from django.shortcuts import render

# Create your views here.

def bangla(request):
    return render(request,'course/courseOne.html')

def english(request):
    return render(request,'course/courseTwo.html')