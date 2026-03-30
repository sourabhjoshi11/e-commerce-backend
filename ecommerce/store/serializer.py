from rest_framework import serializers

from .models import Products,Category,Customer,Orders,Cart

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
                model=Products
                fields='__all__'



class CategorySerializer(serializers.ModelSerializer):
        class Meta:
                model=Category
                fields='__all__'


class CustomerSerializer(serializers.ModelSerializer):
        class Meta:
                model=Customer
                fields=['name','phone','email']




class OrderSerializer(serializers.ModelSerializer):
        class Meta:
                model=Orders
                fields='__all__'


class CartSerializer(serializers.ModelSerializer):
        class Meta:
                model=Cart
                fields='__all__'


from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
        password=serializers.CharField(write_only=True)
        class Meta:
                model=User
                fields=['username','password']

        def create(self,validated_data):
                 user=User.objects.create_user(
                                username=validated_data['username'],
                                password=validated_data['password']
                        )

                 return user