from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created = models.DateTimeField()


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField()
