from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

class Organization(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)