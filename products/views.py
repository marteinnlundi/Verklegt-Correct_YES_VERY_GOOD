from django.shortcuts import render


# TODO: Show all menu items
def menu(request):
    return render(request, 'products/menu.html')

def offers(request):
    return render(request, 'products/offers.html')




# Create your views here.

# TODO: Filter items on menu by type
def filter_by_type(request):
    pass

# TODO: Search for item by name
def search_by_name(request):
    pass

# TODO: Open detailed product display
def product_detail(request, product_id):
    pass


# TODO: Show all offer items
def offer(request):
    pass

# TODO: Add item to shopping cart from menu or offer
def add_to_cart(request, product_id):
    pass

# TODO: Add menu items to offer
def add_menu_to_offer(request):
    pass


# Filter Items on Menu by Type

# The filter by type view is responsible for displaying only certain types of menu items. Here are some of the tasks that the filter by type view should perform:

# TODO:Retrieve the menu items from the database.
# TODO:Allow the customer to select a type of menu item to display.
# TODO:Display only the selected type of menu item.

# Search for Item by Name

# The search by name view is responsible for allowing the customer to search for a menu item by name. Here are some of the tasks that the search by name view should perform:

# TODO:Retrieve the menu items from the database.
# TODO:Allow the customer to enter a search term.
# TODO:Display only the menu items that match the search term.

# Open Detailed Product Display

# The product detail view is responsible for displaying detailed information about a menu item, such as its name, description, price, and ingredients. Here are some of the tasks that the product detail view should perform:

# TODO:Retrieve the selected menu item from the database.
# TODO:Display the menu item's name, description, price, and ingredients.
# TODO:Allow the customer to add the item to their shopping cart.

# Show All Menu Items

# The menu view is responsible for displaying all the menu items. Here are some of the tasks that the menu view should perform:

# TODO:Retrieve all the menu items from the database.
# TODO:Display all the menu items in a table or list format.
# TODO:Allow the customer to add an item to their shopping cart.

# Show All Offer Items

# The offer view is responsible for displaying all the offer items, such as "Buy One, Get One Free". Here are some of the tasks that the offer view should perform:

# TODO:Retrieve all the offer items from the database.
# TODO: Display all the offer items in a table or list format.
# TODO:Allow the customer to add an offer item to their shopping cart.

# Add Item to Shopping Cart from Menu or Offer

# The add to cart view is responsible for adding an item to the customer's shopping cart. Here are some of the tasks that the add to cart view should perform:

# TODO:Retrieve the selected menu or offer item from the database.
# TODO:Add the item to the customer's shopping cart.
# TODO:Redirect the customer to the shopping cart page.

# Add Menu Items to Offer

# The add menu to offer view is responsible for allowing the user to add items from the menu to their offer choose pizza for the 2 for 1

# TODO: 
# TODO:
# TODO:
