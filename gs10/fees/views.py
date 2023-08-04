from django.shortcuts import render

# Create your views here.
def bangla(request):
    return render(request, 'fees/feesOne.html')


def english(request):
    return render(request, 'fees/FeesTwo.html')