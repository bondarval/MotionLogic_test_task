from django.db import models


class Restaurant(models.Model):
    franchise = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=50)
