from django import forms
from users.models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'user__username']

    profile_picture = forms.ImageField(required=False, label='Profile Picture')
    user__username = forms.CharField(required=True, label='Username')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'name', 'email']
        
    img = forms.ImageField(required=False, label='Profile Picture')
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    