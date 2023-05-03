from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about-us.html')

def profiles(request):
    return render(request, 'users/profiles.html')
