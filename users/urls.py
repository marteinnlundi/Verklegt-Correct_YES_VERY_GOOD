from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path



urlpatterns = [

    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('myprofile', views.myprofile_view, name='myprofile'),
    path('edit_profile', views.edit_profile_view, name='edit_profile'),
    # breyta i register ? 
    path('signin', views.signin_view, name='signin'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
   
]