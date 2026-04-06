from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from employees.forms import EmployeeForm
from employees.models import EmployeeModel


class ViewEmployees(LoginRequiredMixin, ListView):
    template_name = 'employees/employees-list.html'
    context_object_name = 'employees'
    paginate_by = 12

    def get_queryset(self):
        qs = self.request.GET.get('q', '')

        employees = EmployeeModel.objects.filter(company=self.request.user.businessuser)
        if qs:
            employees = employees.filter(Q(first_name__icontains=qs) | Q(last_name__icontains=qs))
        return employees

class AddEmployee(LoginRequiredMixin, CreateView):
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = 'employees/add-employee.html'
    success_url = reverse_lazy('employees:employees_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.company = self.request.user.businessuser
        return super().form_valid(form)

class EditEmployee(LoginRequiredMixin, UpdateView):
    template_name = 'employees/edit-employee.html'
    slug_url_kwarg = 'employee_slug'
    slug_field = 'slug'
    form_class = EmployeeForm

    def get_object(self, queryset=None):

        slug = self.kwargs.get(self.slug_url_kwarg)

        employee = EmployeeModel.objects.filter(slug=slug).first()

        if employee:
            return employee

        raise Http404('Employee not found')

    def get_success_url(self):
        return reverse(
            'employees:employee_details',
            kwargs={
                'employee_slug': self.object.slug
            }
        )

class DeleteEmployee(LoginRequiredMixin, DeleteView):
    template_name = 'employees/delete-employee.html'
    slug_url_kwarg = 'employee_slug'
    success_url = reverse_lazy('employees:employees_list')

    def get_object(self, queryset=None):

        slug = self.kwargs.get(self.slug_url_kwarg)

        employee = EmployeeModel.objects.filter(slug=slug).first()

        if employee:
            return employee

        raise Http404('Employee not found')

class EmployeeDetails(LoginRequiredMixin, DetailView):
    template_name = 'employees/employee-details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'employee_slug'

    def get_object(self, queryset = None):

        slug = self.kwargs.get('employee_slug')

        employee = EmployeeModel.objects.filter(slug=slug).first()

        if employee:
            return employee

        raise Http404('Employee not found')