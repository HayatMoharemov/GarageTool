from django.contrib import admin

from employees.models import EmployeeModel


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'hired_at']
    search_fields = ['first_name']