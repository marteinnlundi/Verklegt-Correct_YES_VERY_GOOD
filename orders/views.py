import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PaymentForm
from products.models import Products, Offers
from decimal import Decimal
from users.models import Profile
from django.contrib.auth.decorators import login_required
import datetime

size_prices = {'small': 0, 'medium': 500, 'large': 1000}
@login_required
def cart_view(request):
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
        size = request.GET.get('size', 'small')
        price = Decimal(item['price']) + size_prices[size]
        quantity = item['quantity']
        total_price = price * quantity
        cart_total += total_price
        cart_items.append({
            'id': item_id,
            'name': item['name'],
            'price': price,
            'quantity': quantity,
            'total_price': total_price,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'user_profile': user_profile,
    }

    return render(request, 'cart.html', context)

def checkout(request):
    form = PaymentForm()
    if request.method == 'POST':
        payment_method = request.POST.get('payment-method')
        if payment_method == 'pay-at-pickup':
            return redirect('confirmation')
        elif payment_method == 'pay-with-card':
            form = PaymentForm(request.POST)
            if form.is_valid():
                return redirect('confirmation')
    return render(request, 'checkout.html', {'form': form})

def add_to_cart(request, product_id):
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
        cart[product_id] = {'name': product.name, 'price': str(price), 'quantity': quantity}

    request.session['cart'] = cart
    return redirect('cart')

def add_offer_to_cart(request, offer_id):
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
    request.session['cart'] = {}
    messages.success(request, 'Cart cleared successfully!')
    return redirect('cart')

def confirmation_view(request):
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
            'price': price,
            'quantity': quantity,
            'total_price': total_price,
        })

    # Clear the cart
    request.session['cart'] = {}

    # Pass the order details to the template context
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'delivery_time': datetime.datetime.now() + datetime.timedelta(minutes=30),
    }
    return render(request, 'confirmation.html', context)



def change_item_quantity(request, item_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if quantity <= 0:
        del cart[str(item_id)]
    else:
        cart[str(item_id)]['quantity'] = quantity
    request.session['cart'] = cart
    return redirect('cart')

def remove_item(request, item_id):
    cart = request.session.get('cart', {})
    del cart[str(item_id)]
    request.session['cart'] = cart
    return redirect('cart')

def review_order(request):
    cart = request.session.get('cart', {})
    cart_items = []

    size_prices = {'small': 0, 'medium': 500, 'large': 1000}

    for item_id, item in cart.items():
        product = Products.objects.get(id=item_id)
        size = request.POST.get('size', 'small')
        price = Decimal(item['price']) + size_prices[size]
        quantity = item['quantity']
        total_price = price * quantity
        cart_items.append({
            'id': item_id,
            'name': item['name'],
            'price': price,
            'quantity': quantity,
            'total_price': total_price,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': sum(item['total_price'] for item in cart_items),
    }

    return render(request, 'review_order.html', context=context)
