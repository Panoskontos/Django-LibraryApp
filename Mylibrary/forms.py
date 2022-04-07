from django.forms import forms, ModelForm
from .models import *


class AuthorRegistartionForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class PublisherForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
