from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('myprofile', views.myprofile_view, name='myprofile'),
    path('edit_profile', views.edit_profile_view, name='edit_profile'),
    path('login', views.login_view, name='login'),
    path('signin', views.signin_view, name='signin'),
]