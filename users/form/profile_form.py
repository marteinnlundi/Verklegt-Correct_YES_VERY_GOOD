from django import forms
from users.models import Profile
from django.contrib.auth.models import User

# User registration form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'name', 'email', 'password']

    profile_picture = forms.ImageField(required=False, label='Profile Picture')
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Password')



# Edit user form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture', 'name', 'email', 'password']

    profile_picture = forms.ImageField(required=False, label='Profile Picture')
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Password')
