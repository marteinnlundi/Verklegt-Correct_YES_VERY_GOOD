from django.urls import path
from . import views

# admin localhost:8000/admin

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('profiles/', views.profiles, name="profiles"),
]
