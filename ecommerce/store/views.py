from django.shortcuts import render

from rest_framework import viewsets

from .serializer import ProductSerializer,CategorySerializer,CustomerSerializer,OrderSerializer
from .models import Products,Orders,Customer,Category


from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({
        "products": "/app/products/",
        "customers": "/app/customer/",
        "orders": "/app/order/",
        "categories": "/app/category/"
    })

from .serializer import RegisterSerializer

@api_view(['POST'])
def Register(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'user created'})
    return Response(serializer.errors)




class ProductViewSet(viewsets.ModelViewSet):

    queryset=Products.objects.all()
    serializer_class=ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset=Orders.objects.all()
    serializer_class=OrderSerializer

