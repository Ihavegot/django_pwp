from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Menu(models.Model):
    dishName = models.CharField(max_length=30)
    dishPrice = models.CharField(max_length=10)
    dishDescription = models.CharField(max_length=200)
    dishPicture = models.CharField(max_length=30)

    def __str__(self):
        return self.dishName + self.dishPrice + self.dishDescription + self.dishPicture


class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.JSONField()
    phone = models.CharField(max_length=15)
    adres = models.CharField(max_length=100)
    info = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
