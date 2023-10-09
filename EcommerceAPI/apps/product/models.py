from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)
    category = TreeForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name