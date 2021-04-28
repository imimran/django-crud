from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=100)
    addrress = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)