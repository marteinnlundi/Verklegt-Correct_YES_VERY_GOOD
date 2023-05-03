from django.shortcuts import render

# orders = [
#     { 'id': 1, 'name': 'Pepperoni Pizza', 'price': 10.99 },
#     { 'id': 2, 'name': 'Cheese Pizza', 'price': 9.99 },
#     { 'id': 3, 'name': 'Veggie Pizza', 'price': 11.99 },
# ]

# Create your views here.

def cart(request):
    return render(request, 'orders/cart.html')
