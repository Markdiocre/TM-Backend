from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, Category, Product,OrderDetail, Order

from .serializers import CompanySerializer, CategorySerializer, ProductSerializer, OrderDetailSerializer, OrderSerializer

# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filterset_fields = ('user',)
    

class CategoryView(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filterset_fields = ('company_id',)
    


class ProductView(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filterset_fields = ('company_id',)
    

class OrderView(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated, ]
    filterset_fields = ('company_id',)
    
    

    def get_queryset(self):
        company = self.request.user.company
        print(company)
        return Order.objects.filter(company_id=company)

    def create(self, request):
        print(request.data)
        order = Order.objects.create(
            company_id = self.request.user.company,
            customer_name = request.data['customer_name'],
            customer_number = request.data['customer_number'],
            customer_address = request.data['customer_address']
        )

        
        for ord in request.data['order_detail_id']:
            o = OrderDetail.objects.create(product_id=Product.objects.get(product_id = ord['product_id']), quantity = ord['quantity'])
            order.order_detail_id.add(o)
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)

# class InvoiceView(viewsets.ModelViewSet):
#     serializer_class = InvoiceSerializer
#     permission_classes = [IsAuthenticated, ]

#     def get_queryset(self):
#         company = self.request.user.company
#         print(company)
#         return Invoice.objects.filter(company_id=company)
