from django.contrib import admin

from garage.models import CarModel, MotorcycleModel


class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'engine_displacement','created_at','is_repaired']
    list_filter = ['is_repaired']
    search_fields = ['make', 'model', 'created_at', 'id']

@admin.register(CarModel)
class CarModelAdmin(BaseModelAdmin):
    pass

@admin.register(MotorcycleModel)
class MotorcycleAdmin(BaseModelAdmin):
    pass