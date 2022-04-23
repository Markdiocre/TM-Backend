from django.shortcuts import render
from rest_framework import viewsets

from .models import Company, Category, Product,OrderDetail, Order, Invoice

from .serializers import CompanySerializer, CategorySerializer, ProductSerializer, OrderDetailSerializer, OrderSerializer, InvoiceSerializer

# Create your views here.


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


