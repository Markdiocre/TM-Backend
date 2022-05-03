from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryView, CompanyView, OrderView, ProductView

router = DefaultRouter()
router.register('company', CompanyView,basename='company')
router.register('category', CategoryView,basename='category')
router.register('product', ProductView,basename='product')
router.register('order', OrderView, basename='order')
# router.register('invoice',InvoiceView, basename='invoice')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
] + router.urls