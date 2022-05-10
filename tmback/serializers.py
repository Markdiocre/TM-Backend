from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer
from .models import Company, Category, Product,OrderDetail, Order

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'user', 'company_name','company_address','company_number']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'company_id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'category_id', 'company_id','name','description','price']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['order_detail','product_id','quantity']

class OrderSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    class Meta:
        model = Order
        fields = ['order_id','company_id','order_detail_id','customer_name','customer_number','customer_address','date_ordered','status']



# class InvoiceSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         super(InvoiceSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         if request and (request.method == 'POST' or request.method == 'PUT'):
#             self.Meta.depth = 0
#         else:
#             self.Meta.depth = 1
    
#     class Meta:
#         model = Invoice
#         fields = ['invoice_id','company_id','order_id','date_delivered']

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'email','username', 'first_name', 'last_name', 'password', )

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('id','username', 'email', 'first_name','last_name',)