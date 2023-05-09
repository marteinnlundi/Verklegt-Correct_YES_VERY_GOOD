from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('confirmation/', confirmation_view, name='confirmation'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('change-item-quantity/<int:item_id>/', change_item_quantity, name='change_item_quantity'),
    path('remove-item/<int:item_id>/', remove_item, name='remove_item'),
    path('review_order/', review_order, name='review_order'),
    path('add-offer-to-cart/<int:offer_id>/', add_offer_to_cart, name='add_offer_to_cart'),

]
