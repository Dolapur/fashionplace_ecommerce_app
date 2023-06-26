from django import forms
from .models import Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Username'
    }))

    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Email Address'
    }))

    password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'At least eight characters'
    }))
    password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']