from django.db import models


class Menu(models.Model):
    dishName = models.CharField(max_length=30)
    dishPrice = models.CharField(max_length=10)
    dishDescription = models.CharField(max_length=200)
    dishPicture = models.CharField(max_length=30)

    def __str__(self):
        return self.dishName + self.dishPrice + self.dishDescription + self.dishPicture
