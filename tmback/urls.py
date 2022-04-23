from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CompanyView

router = DefaultRouter()
router.register('company', CompanyView,basename='company')

urlpatterns = router.urls