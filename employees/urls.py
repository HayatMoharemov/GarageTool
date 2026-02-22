from django.urls import path

from employees.views import ViewEmployees, AddEmployee, EmployeeDetails, EditEmployee, DeleteEmployee

app_name = 'employees'

urlpatterns = [
    path('', ViewEmployees.as_view(),name='employees_list'),
    path('add_employee/', AddEmployee.as_view(), name='add_employee'),
    path('details/<slug:employee_slug>', EmployeeDetails.as_view(), name='employee_details'),
    path('details/<slug:employee_slug>/edit', EditEmployee.as_view(), name='employee_edit'),
    path('details/<slug:employee_slug>/delete', DeleteEmployee.as_view(), name='delete_employee'),
]