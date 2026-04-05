from rest_framework import serializers

from garage.models import VehicleTypeBaseModel, MotorcycleModel, CarModel


class VehicleBaseSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = VehicleTypeBaseModel
        fields = (
            'id',
            'type',
            'owner',
            'make',
            'model',
            'production_date',
            'mileage',
            'engine_displacement',
            'horsepower',
            'fuel_type',
        )
        extra_kwargs = {
            'owner': {'read_only': True},
            'type': {'read_only': True}
        }

    def validate_mileage(self, value):
        if value < 0:
            raise serializers.ValidationError('Mileage cannot be negative')
        return value

    def validate_horsepower(self, value):
        if value < 0:
            raise serializers.ValidationError('Horsepower cannot be negative')
        return value

    def validate_engine_displacement(self, value):
        if value < 0:
            raise serializers.ValidationError('Engine displacement cannot be negative')
        return value

class MotorcycleSerializer(VehicleBaseSerializer):
    class Meta(VehicleBaseSerializer.Meta):
        model = MotorcycleModel
        fields = VehicleBaseSerializer.Meta.fields + ('engine_type',)
        extra_kwargs = {
            'fuel_type': {'read_only': True}
        }

class CarSerializer(VehicleBaseSerializer):
    class Meta(VehicleBaseSerializer.Meta):
        model = CarModel