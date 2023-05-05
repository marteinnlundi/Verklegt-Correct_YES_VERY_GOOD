from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def myprofile_view(request):
    return render(request, 'myprofile.html')

def edit_profile_view(request):
    return render(request, 'edit_profile.html')

def login_view(request):
    return render(request, 'login.html')

def signin_view(request):
    return render(request, 'signin.html')
