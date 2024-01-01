from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder' : 'Enter your name',
            'class' : 'form-control rounded'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Enter you email address',
        'class' : 'form-control rounded'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' :'Enter your password',
        'class':'form-control rounded'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' :'Confirm your password',
        'class':'form-control rounded'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your username',
        'class' : 'form-control rounded'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter your password',
         'class' : 'form-control rounded'
    }))