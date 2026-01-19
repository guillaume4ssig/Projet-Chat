from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="Email ",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': "Email"})
    )
    username = forms.CharField(
        label="Nom d'utilisateur ",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Nom d'utilisateur"})
    )
    password1 = forms.CharField(
        label="Mot de passe ",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Mot de passe"})
    )
    password2 = forms.CharField(
        label="Confirmation ",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Confirmation"})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur ",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Nom d'utilisateur"})
    )
    password = forms.CharField(
        label="Mot de passe ",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Mot de passe"})
    )