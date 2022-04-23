from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryView, CompanyView, InvoiceView, OrderView, ProductView

router = DefaultRouter()
router.register('company', CompanyView,basename='company')
router.register('category', CategoryView,basename='category')
router.register('product', ProductView,basename='product')
router.register('order', OrderView, basename='order')
router.register('invoice',InvoiceView, basename='invoice')

urlpatterns = router.urls