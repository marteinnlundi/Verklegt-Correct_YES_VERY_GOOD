from django.shortcuts import render,redirect

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from orders.models import UserOrder
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
            # profile.email = form.cleaned_data['email']
            profile.password = form.cleaned_data['password1']
            profile.save()
            return redirect('/users/login/')
    else:
        form = UserCreationForm()
    return render(request, 'users/signin.html', {'form': form})
    


def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.user.id:
        if request.method == 'POST':
            form = UserEditForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been updated!')
            return render(request, 'users/myprofile.html', { 'user_profile': profile})
        else:
            form = UserEditForm(instance=request.user.profile)
        return render(request, 'users/edit_profile.html', {'form': form})
   


def myprofile_view(request):
    user_profile = Profile.objects.get(user=request.user)
    user_orders = UserOrder.objects.filter(user=request.user)
    orders = []
    for order in user_orders:
        if order.product:
            name = order.product.name
            description = order.product.description
        elif order.offer:
            name = order.offer.name
            description = order.offer.description
        else:
            name = 'Unknown'
            description = 'Unknown'
        orders.append({
            'name': name,
            'description': description,
            'date': order.date,
        })
        
    orders.sort(key=lambda x: x['date'], reverse=True)

    # keep only the first four elements
    orders = orders[:4]

    context = {
        'orders': orders,
        'user_profile': user_profile,
    }

    #if the profile picture is not uploaded, use the default picture
    if not user_profile.profile_picture:
        user_profile.profile_picture = '/default.jpg'
        user_profile.save()

    return render(request, 'users/myprofile.html', context)

  
def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')


from products.models import Offers
import random


def home_view(request):
    offers = Offers.objects.all()
    current_offer = random.choice(offers)
    context = {
        'current_offer': current_offer,
    }
    return render(request, 'home.html', context)