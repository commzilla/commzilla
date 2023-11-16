from django.shortcuts import render

# Create your views here.
def learn_django_course(request):
    return render(request, 'course/home.html', {'title': 'Learn Django','cname':'Django'})