from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title 
    


class User(models.Model):
    fullname = models.CharField(max_length=100)
    adddress = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)