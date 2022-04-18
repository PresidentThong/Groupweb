from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField
    name_pro=models.TextField
    input_date=models.TimeField
    out_date=models.TimeField
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " (" + self.name_en + ")"
