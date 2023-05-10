from django.shortcuts import render
from .models import Products
from. models import Offers


def menu_view(request):
    """
    A view to return the menu page
    
    Args:
    request (HttpRequest): HTTP request object.
        
    Returns:
    HttpResponse: HTTP response object.
    """
    search_query = request.GET.get('search')
    product_type = request.GET.get('type')
    
    pizzas = Products.objects.filter(type='pizza').order_by('name')
    sides = Products.objects.filter(type='side').order_by('name')
    drinks = Products.objects.filter(type='drink').order_by('name')

    if product_type:
        pizzas = pizzas.filter(type=product_type)
        sides = sides.filter(type=product_type)
        drinks = drinks.filter(type=product_type)

    if search_query:
        pizzas = pizzas.filter(description__icontains=search_query)
        sides = sides.filter(description__icontains=search_query)
        drinks = drinks.filter(description__icontains=search_query)

    for side in sides:
        side.price = '{:,.0f}kr'.format(side.price).replace(',', '.')
    for drink in drinks:
        drink.price = '{:,.0f}kr'.format(drink.price).replace(',', '.')

    context = {
        'pizzas': pizzas,
        'sides': sides,
        'drinks': drinks,
    }
    return render(request, 'menu.html', context)


def menu_item_view(request):
    """
    A view to return the menu item page
    
    Args:
    request (HttpRequest): HTTP request object.
    
    Returns:
    HttpResponse: HTTP response object.
    """
    product_id = request.GET.get('id')
    product = Products.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'menu-item.html', context)


def offers_view(request):
    """
    A view to return the offers page
    
    Args:
    request (HttpRequest): HTTP request object.
    
    Returns:
    HttpResponse: HTTP response object.
    """
    offers = Offers.objects.all()
    for offer in offers:
        offer.price = '{:,.0f}kr'.format(offer.price).replace(',', '.')
    context = {'offers': offers}
    return render(request, 'offers.html', context)


def offer_item_view(request):
    """
    A view to return the offer item page
    
    Args:
    request (HttpRequest): HTTP request object.
    
    Returns:
    HttpResponse: HTTP response object.
    """
    offer_id = request.GET.get('id')

    offer = Offers.objects.get(id=offer_id)
    offer.price = '{:,.0f}kr'.format(offer.price).replace(',', '.')

    context = {'offer': offer}
    return render(request, 'offer-item.html', context)




