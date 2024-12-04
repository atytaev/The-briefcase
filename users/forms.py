from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(1900, 2025)))
    phone_number = forms.CharField(max_length=15, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'phone_number', 'profile_picture', 'password1', 'password2')