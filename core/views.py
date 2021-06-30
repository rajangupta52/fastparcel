from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def HomePageView(request):
    return render(request, 'HomePageView.html')

@login_required()
def CustomerPageView(request):
    return render(request, 'HomePageView.html')

@login_required()
def CourierPageView(request):
    return render(request, 'HomePageView.html')

def SignUpPageView(request):
    form = forms.SignUpForm()
    if request.method =='POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request, user)
            return redirect('/')
    return render(request, 'sign_up.html',{'form':form})