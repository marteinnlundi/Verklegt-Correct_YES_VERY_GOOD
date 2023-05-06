from django.shortcuts import render,redirect

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

#  register form 
def signin_view(request):
       
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login/')
    return render(request, 'users/signin.html', {
        'form': UserCreationForm(),   
    })


def login_view(request):
    return render(request, 'users/login.html')

def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def myprofile_view(request):
    return render(request, 'myprofile.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .form.profile_form import UserProfileForm

def edit_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/users/myprofile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'users/edit_profile.html', {'form': form})

