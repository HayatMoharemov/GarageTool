from django.urls import path, include
from rest_framework.routers import SimpleRouter

from vehicles_api import views

router = SimpleRouter()

router.register('motorcycles', views.MotorcycleViewSet, basename='motorcycles')
router.register('cars', views.CarViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
    ]