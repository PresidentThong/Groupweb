from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)
    description = models.TextField()
    
class Product(models.Model):
    code = models.CharField(max_length=20)
    name_pro=models.TextField
    input_date=models.TimeField
    out_date=models.TimeField
    category=models.ForeignKey(Category, on_delete=models.CASCADE)