from django.shortcuts import render

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def confirmation_view(request):
    return render(request, 'confirmation.html')