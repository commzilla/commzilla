from django.shortcuts import render


# Create your views here.
def django_fees(request):
    context = {
        'title': 'Django Fees',
        'cname': 'Django',
        'charge': 300
    }
    return render(request, 'fees/home.html', context=context)
