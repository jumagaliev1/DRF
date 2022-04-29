from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Cities'

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Categories'
class Product(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    upload_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
