from django import forms
from users.models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'user__username']

    profile_picture = forms.ImageField(required=False, label='Profile Picture')
    user__username = forms.CharField(required=True, label='Username')

