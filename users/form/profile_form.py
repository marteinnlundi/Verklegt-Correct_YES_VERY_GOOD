from django import forms
from users.models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'name']

    profile_picture = forms.ImageField(required=False, label='Profile Picture')
    name = forms.CharField(required=True, label='Name')
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'name']

    profile_picture = forms.ImageField(required=False, label='Profile Picture')
    name = forms.CharField(required=True, label='Name')
    