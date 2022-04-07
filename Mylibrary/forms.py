from django.forms import ModelForm
from matplotlib import widgets
from .models import *
from django import forms


class AuthorRegistartionForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class PublisherForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }
