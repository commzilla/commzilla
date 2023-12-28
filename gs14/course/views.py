from django.shortcuts import render

# Create your views here.
def course_list(request):
    details = {'b': 300, 'e': 400, 'm': 500, 's':500}
    return render(request, 'course/home.html', context=details)