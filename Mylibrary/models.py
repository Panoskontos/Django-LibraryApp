from django.db import models
from django.contrib.auth.models import AbstractUser

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
