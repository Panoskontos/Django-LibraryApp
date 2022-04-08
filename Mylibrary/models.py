from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Publisher', 'Publisher'),
        ('Author', 'Author'),
        ('LibraryUser', 'LibraryUser'),
        ('Admin', 'Admin'),
    )

    user_type = models.CharField(max_length=100,
                                 choices=USER_TYPE_CHOICES, null=True)
    user_balance = models.PositiveSmallIntegerField(null=True, blank=True)


class Publisher(models.Model):
    user = models.OneToOneField(
        CustomUser, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return(self.name)


class LibraryUser(models.Model):
    user = models.OneToOneField(
        CustomUser, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return(self.name)


class Author(models.Model):
    user = models.OneToOneField(
        CustomUser, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return(self.name)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, blank=True)
    publication_date = models.DateField()
    STARS = (
        ('1 star', '1 star'),
        ('2 star', '2 star'),
        ('3 star', '3 star'),
        ('4 star', '4 star'),
    )
    num_stars = models.CharField(max_length=50,
                                 choices=STARS, null=True, blank=True)
    number_of_rates = models.IntegerField(default=0)
    book = models.FileField()

    def __str__(self):
        return(self.title)


class Favorites(models.Model):
    publisher = models.ForeignKey(
        Publisher, null=True, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
