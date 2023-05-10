from django.shortcuts import get_object_or_404, render,redirect

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from orders.models import UserOrder
from users.form.profile_form import UserEditForm
from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .form.profile_form import UserEditForm
from products.models import Offers
import random

#  register form, save the user to the user_profile table
def signin_view(request):
    """
    Render the signin page, and handle user registration.

    If the user is already logged in, they are redirected to the home page.
    If the request is a POST request, the UserCreationForm is validated and the user is saved.
    A new Profile instance is created and saved, using the information from the UserCreationForm.
    Finally, the user is redirected to the login page.
    """
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.name = form.cleaned_data['username']
            # profile.email = form.cleaned_data['email']
            # eg skill ekkert 
            profile.password = form.cleaned_data['password1']
            profile.save()
            print(form.cleaned_data)

            return redirect('/users/login/')
    else:
        form = UserCreationForm()

    return render(request, 'users/signin.html', {'form': form})

def edit_profile_view(request):
    """
    Render the edit profile page, and handle user profile updates.

    If the user is not logged in, they are redirected to the login page.
    If the request is a POST request, the UserEditForm is validated and the user is saved.
    Finally, the user is redirected to the myprofile page.
    """
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
    """
    Render the myprofile page, and display the user profile.
    
    If the user is not logged in, they are redirected to the login page.
    If the user profile picture is not uploaded, the default picture is used.
    """
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
    """
    Render the index page.
    """
    return render(request, 'index.html')


# def home_view(request):
#     """
#     Render the home page.
#     """
#     return render(request, 'home.html')


def about_view(request):
    """
    Render the about page.
    """
    return render(request, 'about.html')


def home_view(request):
    """
    Render the home page with rotating offers.
    """
    offers = Offers.objects.all()
    context = {
        'offers': offers,
    }
    return render(request, 'home.html', context)

def add_to_cart_view(request, order_id):
    """
    Add an order to the cart.
    """
    order = UserOrder.objects.get(id=order_id)
    order.in_cart = True
    order.save()
    return redirect('cart')
