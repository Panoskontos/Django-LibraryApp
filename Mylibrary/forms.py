from django.forms import ModelForm
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


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['number_of_rates', 'num_stars', 'id']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    new_password_repeat = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }
