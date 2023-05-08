from django.urls import path
from .views import cart_view, checkout_view, confirmation_view, add_to_cart, clear_cart, change_item_quantity, remove_item, review_order

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('confirmation/', confirmation_view, name='confirmation'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('change-item-quantity/<int:item_id>/', change_item_quantity, name='change_item_quantity'),
    path('remove-item/<int:item_id>/', remove_item, name='remove_item'),
    path('review_order/', review_order, name='review_order'),
]
