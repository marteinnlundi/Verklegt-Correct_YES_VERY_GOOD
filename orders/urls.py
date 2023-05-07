from django.urls import path
from .views import cart_view, checkout_view, confirmation_view

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('confirmation/', confirmation_view, name='confirmation'),  # <-- add this line]
]