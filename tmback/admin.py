from django.contrib import admin

from .models import Company, Category, Product, OrderDetail, Order, Invoice

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_address', 'company_number')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'price')

class OrderDetailAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_number','customer_address','date_ordered', 'status')

class InvoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)