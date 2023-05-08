from django.shortcuts import render,redirect

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from users.form.profile_form import UserEditForm
from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .form.profile_form import UserEditForm

#  register form, save the user to the user_profile table
def signin_view(request):
    if request.user.id:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            profile = Profile()
            profile.user = form.instance
            profile.name = form.cleaned_data['username']
            profile.email = form.cleaned_data['email']
            profile.password = form.cleaned_data['password1']
            profile.save()
            return redirect('/users/login/')
    else:
        form = UserCreationForm()
    return render(request, 'users/signin.html', {'form': form})
    


#edit profile form, update the user to the user_profile table
def edit_profile_view(request):
    if request.user.id:
        if request.method == 'POST':
            form = UserEditForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been updated!')
                profile = Profile.objects.get(user=request.user)
            return render(request, 'users/myprofile.html', { 'user_profile': profile})
        else:
            form = UserEditForm(instance=request.user.profile)
        return render(request, 'users/edit_profile.html', {'form': form})
   


def myprofile_view(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'users/myprofile.html', {'user_profile': user_profile})


def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')



