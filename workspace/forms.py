from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from account.models import *

# class NFTForm(forms.Form):
#     name = forms.CharField(
#         max_length=255, 
#         label='Название', 
#         widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     creator = forms.ModelChoiceField(
#         queryset=Artist.objects.all(), 
#         label='Создатель',
#         widget=forms.Select(attrs={
#             'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
#         }))
#     price = forms.DecimalField(
#         max_digits=10, 
#         decimal_places=2, 
#         label='Цена',
#         widget=forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     highest_bid = forms.DecimalField(
#         max_digits=10, 
#         decimal_places=2, 
#         label='Высшая ставка', 
#         required=False,
#         widget=forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     image_url = forms.URLField(
#         label='URL Изображения', 
#         required=False,
#         widget=forms.URLInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     minted_date = forms.DateField(
#         label='Дата создания', 
#         widget=forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'}),
#         required=False
#     )

# class InformationForm(forms.Form):
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'}),
#         label='Описание'
#     )
#     blockchain = forms.CharField(
#         max_length=255, 
#         initial='Ethereum', 
#         label='Блокчейн',
#         widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     etherscan_link = forms.URLField(
#         label='Etherscan', 
#         required=False,
#         widget=forms.URLInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     original_link = forms.URLField(
#         label='Оригинальная ссылка', 
#         required=False,
#         widget=forms.URLInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'})
#     )
#     tags = forms.ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         widget=forms.CheckboxSelectMultiple(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'}),
#         label='Тэги',
#         required=False
#     )

class NFTForm(forms.ModelForm):
    class Meta:
        model = NFT
        fields = ['name', 'creator', 'price', 'highest_bid', 'image_url', 'minted_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'creator': forms.Select(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'highest_bid': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'minted_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
        }

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['description', 'blockchain', 'etherscan_link', 'original_link', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'blockchain': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'etherscan_link': forms.URLInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'original_link': forms.URLInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'mt-1 block w-full focus:outline-none focus:ring-2 focus:ring-green-500 sm:text-sm'
            }),
        }


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
