from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    
