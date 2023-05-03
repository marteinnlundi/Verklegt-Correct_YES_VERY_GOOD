"""
URL configuration for PizzaLair project.

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

from django.urls import path, include

# admin localhost:8000/admin

urlpatterns = [ 
    path('', include('users.urls')),
    path('home/', include('users.urls')),
    path('about/', include('users.urls')),
    path('profiles/', include('users.urls')),
    path('offers/', include('products.urls')), 
    path('menu/', include('products.urls')),
    path('cart/', include('orders.urls')),
]