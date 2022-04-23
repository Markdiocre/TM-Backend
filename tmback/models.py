from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=100)
    company_number = models.IntegerField()

    def __str__(self):
        return self.company_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class OrderDetail(models.Model):
    order_detail = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.product_id.name, self.quantity)

class Order(models.Model):

    ord_status = [
        ['P','Pending'],
        ['O','Ongoing'],
        ['D','Done'],
    ]

    order_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    order_detail_id = models.ManyToManyField(OrderDetail)

    customer_name = models.CharField(max_length= 30)
    customer_number = models.IntegerField()
    customer_address = models.CharField(max_length= 100)
    date_ordered = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=ord_status, default='P')

    def __str__(self):
        return self.customer_name

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    date_delivered = models.DateTimeField(auto_now=True)

