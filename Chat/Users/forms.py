from django import forms
from .models import *

class Cadastro_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'mail','password']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})            
        }

class Login_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mail','password']
        
        widgets = {
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }
