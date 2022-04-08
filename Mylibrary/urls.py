from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('author_register', AuthorRegister, name="author_register"),
    path('publisher_register', PublisherRegister, name="publisher_register"),
    path('login/', Login, name="login"),
    path('add-book/', add_book, name="add_book"),
    path('delete-book/<str:pk>', delete_book, name="delete_book"),
    path('update-book/<str:pk>', update_book, name="update_book"),
    path('change_password', change_password, name="change_password"),

]
