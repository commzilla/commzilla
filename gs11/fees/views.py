from django.shortcuts import render

# Create your views here.
def bangla(request):
    return render(request, 'fees/feesone.html')

def english(request):
    return render(request, 'fees/feestwo.html')