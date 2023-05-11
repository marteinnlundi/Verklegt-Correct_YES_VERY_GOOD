import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from orders.models import UserOrder
from .forms import PaymentForm
from products.models import Products, Offers
from decimal import Decimal
from users.models import Profile
from django.contrib.auth.decorators import login_required
import datetime


size_prices = {'small': 0, 'medium': 500, 'large': 1000}

@login_required
def cart_view(request):
    """
    Display the contents of the user's shopping cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the cart template and its context.
    """
    user_profile = Profile.objects.get(user=request.user)
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    
    for item_id, item in cart.items():
        try:
            product = Products.objects.get(id=item_id)
        except Products.DoesNotExist:
            try:
                product = Offers.objects.get(id=item_id)
            except Offers.DoesNotExist:
                return redirect('cart')
        
        size = item.get('size', 'small')
        price = Decimal(str(product.price)) + size_prices.get(size, 0)
        quantity = item['quantity']
        total_price = price * quantity
        cart_total += total_price
        cart_items.append({
            'id': item_id,
            'name': item['name'],
            'price': f"{price} kr",
            'quantity': quantity,
            'total_price': f"{total_price} kr",
        })

    context = {
        'cart_items': cart_items,
        'cart_total': f"{cart_total} kr",
        'user_profile': user_profile,
    }

    return render(request, 'cart.html', context)


def checkout(request):
    """
    Display the checkout page.

    Args:
    request (HttpRequest): The HTTP request object.
    
    Returns:
    HttpResponse: The HTTP response containing the checkout template and its context.
    
    """
    form = PaymentForm()
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        if payment_method == 'pay-with-card':
            print("pay with card")
            form = PaymentForm(request.POST)
            if form.is_valid():
                print("form validated")
                return redirect('confirmation')
            else:
                print("form not valid")
        elif payment_method == 'pay-at-pickup':
            return redirect('confirmation')
    return render(request, 'checkout.html', {'form': form})
from django.utils.crypto import get_random_string




def add_to_cart(request, product_id):
    """
    Add a product to the shopping cart.
    
    Args:
    request (HttpRequest): The HTTP request object.
    product_id (int): The ID of the product to add to the cart.
        
    Returns:
    HttpResponse: The HTTP response redirecting the user to the cart.
    """
    product = Products.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    size = request.GET.get('size', 'small')

    if size == 'medium':
        price = product.price + 500
    elif size == 'large':
        price = product.price + 1000
    else:
        price = product.price
    

    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {
            'name': product.name,
            'price': str(price),
            'quantity': quantity,
            'size': size
        }

    request.session['cart'] = cart
    return redirect('cart')



def add_offer_to_cart(request, offer_id):
    """
    Add an offer to the shopping cart.
    
    Args:
    request (HttpRequest): The HTTP request object.
    offer_id (int): The ID of the offer to add to the cart.
    
    Returns:
    HttpResponse: The HTTP response redirecting the user to the cart.
    """
    offer = Offers.objects.get(id=offer_id)
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    size = request.GET.get('size', 'small')
    

    if offer_id in cart:
        cart[offer_id]['quantity'] += quantity
    else:
        cart[offer_id] = {'name': offer.name, 'price': str(offer.price), 'quantity': quantity}

    request.session['cart'] = cart
    return redirect('cart')


def clear_cart(request):
    """
    Clear the shopping cart.
    
    Args:
    request (HttpRequest): The HTTP request object.
    
    Returns:
    HttpResponse: The HTTP response redirecting the user to the cart.
    """
    request.session['cart'] = {}
    messages.success(request, 'Cart cleared successfully!')
    return redirect('cart')

def confirmation_view(request):
    """
    Display the order confirmation page.
    
    Args:
    request (HttpRequest): The HTTP request object.
        
    Returns:
    HttpResponse: The HTTP response containing the confirmation template and its context.
    """
    cart_items = []
    cart_total = 0

    # Retrieve the order details from the session
    cart = request.session.get('cart', {})
    for item_id, item in cart.items():
        try:
            product = Products.objects.get(id=item_id)
        except Products.DoesNotExist:
            try:
                product = Offers.objects.get(id=item_id)
            except Offers.DoesNotExist:
                return redirect('cart')

        size = request.GET.get('size', 'small')
        price = Decimal(item['price']) + size_prices[size]
        quantity = item['quantity']
        total_price = price * quantity
        cart_total += total_price
        cart_items.append({
            'id': item_id,
            'name': item['name'],
            'price': f"{price} kr",
            'quantity': quantity,
            'total_price': f"{total_price} kr",
        })
    
    cart_total_with_kr = f"{cart_total} kr"

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total_with_kr,
    }

    request.session['cart'] = {}

    return render(request, 'confirmation.html', context)

def change_item_quantity(request, item_id):
    """
    Change the quantity of an item in the shopping cart.
    
    Args:
    request (HttpRequest): The HTTP request object.
    
    Returns:
    HttpResponse: The HTTP response redirecting the user to the cart.
    """
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if quantity <= 0:
        del cart[str(item_id)]
    else:
        cart[str(item_id)]['quantity'] = quantity
    request.session['cart'] = cart
    return redirect('cart')


def remove_item(request, item_id):
    """
    Remove an item from the shopping cart.
    
    Args:
    request (HttpRequest): The HTTP request object.
    
    Returns:
    HttpResponse: The HTTP response redirecting the user to the cart.
    """
    cart = request.session.get('cart', {})
    del cart[str(item_id)]
    request.session['cart'] = cart
    return redirect('cart')



def review_order(request):
    """
    Display the order details for the user to review.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the review order template and its context.
    """
    cart = request.session.get('cart', {})
    cart_items = []

    size_prices = {'small': 0, 'medium': 500, 'large': 1000}

    for item_id, item in cart.items():
        try:
            product = Products.objects.get(id=item_id)
        except Products.DoesNotExist:
            try:
                product = Offers.objects.get(id=item_id)
            except Offers.DoesNotExist:
                return redirect('cart')

        size = request.POST.get('size', 'small')
        price = Decimal(item['price']) + size_prices[size]
        quantity = item['quantity']
        total_price = price * quantity
        total_price = float(f'{total_price:.2f}')
        cart_items.append({
            'id': item_id,
            'name': item['name'],
            'price': f'{price:.2f} kr',
            'quantity': quantity,
            'total_price': total_price,
        })

    context = {
    'cart_items': cart_items,
    'cart_total': '{:.0f} kr'.format(sum(item["total_price"] for item in cart_items)),
    }


    return render(request, 'review_order.html', context=context)