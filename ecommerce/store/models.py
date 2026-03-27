from django.db import models
import datetime
from rest_framework.permissions import IsAdminUser,IsAuthenticated


class Category(models.Model):
    name=models.CharField(max_length=50)
    permission_class=[IsAdminUser]
   
    
    

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Customer(models.Model):
    name=models.CharField(max_length=44)
    phone=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)


    


class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    permission_classes =[IsAuthenticated]

 

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=100,default='',blank=True)
    date=models.DateField(default=datetime.date.today)
    status=models.BooleanField(default=False)
    permission_classes=[IsAuthenticated]

   