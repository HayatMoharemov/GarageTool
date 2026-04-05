from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from garage.models import MotorcycleModel, CarModel
from vehicles_api.serializers import CarSerializer, MotorcycleSerializer
from vehicles_api.utils import OwnerFilterMixin


class MotorcycleViewSet(OwnerFilterMixin, ModelViewSet):

    queryset = MotorcycleModel.objects.all()

    permission_classes = [IsAuthenticated]
    serializer_class = MotorcycleSerializer

    filterset_fields = ['make', 'model']
    ordering_fields = ['id']


class CarViewSet(OwnerFilterMixin, ModelViewSet):

    queryset = CarModel.objects.all()

    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer

    filterset_fields = ['make', 'model']
    ordering_fields = ['id']

