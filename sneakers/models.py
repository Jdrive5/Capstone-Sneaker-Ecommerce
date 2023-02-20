from django.db import models

# Create your models here.

class Sneaker(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)