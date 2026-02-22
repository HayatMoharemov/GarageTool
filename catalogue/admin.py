from django.contrib import admin

from catalogue.models import PartModel, ServiceModel


@admin.register(PartModel)
class PartModelAdmin(admin.ModelAdmin):
    list_display = ['title','manufacturer','price']
    search_fields = ['title']

@admin.register(ServiceModel)
class PartModelAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    search_fields = ['title']