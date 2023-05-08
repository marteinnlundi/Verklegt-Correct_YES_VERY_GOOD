import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PaymentForm
from products.models import Products

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment-method')
        if payment_method == 'pay-at-pickup':
            # Process pay-at-pickup payment
            messages.success(request, 'Payment successful! You will pay at pickup.')
            print('Rendering confirmation page for pay-at-pickup')
            return render(request, 'confirmation.html')
        else:
            form = PaymentForm(request.POST)
            if form.is_valid():
                # Process credit card payment
                messages.success(request, 'Payment successful!')
                print('Rendering confirmation page for credit card payment')
                return render(request, 'confirmation.html')
            else:
                if 'card_number' in form.errors:
                    messages.error(request, form.errors['card_number'][0])
                if 'cardholder_name' in form.errors:
                    messages.error(request, form.errors['cardholder_name'][0])
                if 'expiration_date' in form.errors:
                    messages.error(request, form.errors['expiration_date'][0])
                if 'cvc' in form.errors:
                    messages.error(request, form.errors['cvc'][0])
    else:
        form = PaymentForm()
    return render(request, 'checkout.html', {'form': form})

def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'name': product.name, 'price': str(product.price), 'quantity': quantity}
    request.session['cart'] = cart
    return redirect('cart')

def clear_cart(request):
    request.session['cart'] = {}
    messages.success(request, 'Cart cleared successfully!')
    return redirect('cart')

def confirmation_view(request):
    logging.debug('Rendering confirmation page')
    return render(request, 'confirmation.html')
