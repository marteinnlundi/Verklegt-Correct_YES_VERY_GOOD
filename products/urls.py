"""
URL configuration for Product project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('menu', views.menu_view, name='menu'),
    path('menuItem', views.menu_item_view, name='menuItem'),
    path('offers', views.offers_view, name='offers'),
    path('offerItem', views.offer_item_view, name='offerItem'),
    path('search/', views.search_filter, name='search_filter'),

]




