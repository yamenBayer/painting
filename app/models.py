from email.policy import default
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = models.CharField(max_length=100,default="None")
    address = models.CharField(max_length=100,default="None")
    service =  models.CharField(max_length=100)

    def __str__(self):
        return self.service
