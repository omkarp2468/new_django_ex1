from django.db import models
from django.http import request

# Create your models here.
class Employee(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20) 
  