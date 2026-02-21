from django.urls import path

from garage.views import AddCar, AddBike, ViewGarage

app_name = 'garage'

urlpatterns = [
    path('', ViewGarage.as_view(), name='view_garage'),
    path('add_car/',AddCar.as_view(), name='add_car'),
    path('add_bike/',AddBike.as_view(), name='add_bike'),
]