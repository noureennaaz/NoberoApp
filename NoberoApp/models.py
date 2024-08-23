# models.py
from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=255)
    url = models.URLField(max_length=1024)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    MRP = models.IntegerField()
    last_7_day_sale = models.IntegerField(null=True, blank=True)
    fit = models.CharField(max_length=255, null=True, blank=True)
    fabric = models.CharField(max_length=255, null=True, blank=True)
    neck = models.CharField(max_length=255, null=True, blank=True)
    sleeve = models.CharField(max_length=255, null=True, blank=True)
    pattern = models.CharField(max_length=255, null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

class ProductSKU(models.Model):
    product = models.ForeignKey(Product, related_name='available_skus', on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    sizes = models.JSONField()  # Use JSONField to store an array of sizes
