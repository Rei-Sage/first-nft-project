from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginUser(forms.Form):
    username=forms.CharField(label='Логин',
                             widget=forms.TextInput(attrs={'class':'form-input'}))
    password=forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input'}))