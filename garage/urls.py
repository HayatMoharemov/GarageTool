from django.urls import path

from garage.views import AddCar, AddBike, ViewGarage, VehicleDetail, VehicleEdit, DeleteVehicle

app_name = 'garage'

urlpatterns = [
    path('', ViewGarage.as_view(), name='view_garage'),
    path('add_car/',AddCar.as_view(), name='add_car'),
    path('add_bike/',AddBike.as_view(), name='add_bike'),
    path('details/<slug:vehicle_slug>', VehicleDetail.as_view(), name='vehicle_detail'),
    path('details/<slug:vehicle_slug>/edit', VehicleEdit.as_view(), name='vehicle_edit'),
    path('details/<slug:vehicle_slug>/delete/', DeleteVehicle.as_view(), name='vehicle_delete')
]