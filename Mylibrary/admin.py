from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(LibraryUser)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Favorites)
