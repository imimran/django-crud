from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    parentCategoryId = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category =  models.ManyToManyField(Category)
    #seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING, null =  True)
    buyPrice = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    sellPrice = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    discountPercentage = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    discountAmount = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    # ratings
    isAvailable = models.BooleanField(null=False, default=True)
    isVisible = models.BooleanField(null=False, default=True)


    def __str__(self):
        return str(self.name)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False)
