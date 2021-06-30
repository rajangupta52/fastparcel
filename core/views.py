from django.shortcuts import render

# Create your views here.

def HomePageView(request):
    return render(request, 'HomePageView.html')

def CustomerPageView(request):
    return render(request, 'HomePageView.html')
def CourierPageView(request):
    return render(request, 'HomePageView.html')