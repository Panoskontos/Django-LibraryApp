from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('author_register', AuthorRegister, name="author_register"),
    path('publisher_register', PublisherRegister, name="publisher_register"),
    path('login/', Login, name="login"),

]
