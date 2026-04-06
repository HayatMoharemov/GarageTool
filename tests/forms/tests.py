from django.test import TestCase

from accounts.models import BusinessUser, GeneralUser
from employees.forms import EmployeeForm
from garage.forms import CarForm, MotorcycleForm
from django.contrib.auth import get_user_model
from contact.forms import ContactForm

User = get_user_model()

class SimpleFormsTestCase(TestCase):

    def test_car_form_valid(self):
        data = {
            'make': 'Toyota',
            'model': 'Corolla',
            'production_date': '2020-01-01',
            'engine_displacement': 2.0,
            'mileage': 0,
            'horsepower': 100,
            'repair_status': False,
            'notes': 'Needs oil change',
            'fuel_type': 'DIESEL'
        }
        form = CarForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_car_form_invalid(self):
        data = {
            'make': 'Toyota',
            'model': 'Corolla',
            'production_date': '2020-01-01',
            'engine_displacement': 1000,
            'mileage': 0,
            'horsepower': 100,
            'repair_status': False,
            'notes': 'Needs oil change',
            'fuel_type': 'DIESEL'
        }
        form = CarForm(data=data)
        self.assertFalse(form.is_valid(), form.errors)

    def test_motorcycle_form_valid(self):
        data = {
            'make': 'Honda',
            'model': 'CBR500',
            'production_date': '2019-05-01',
            'engine_displacement': 500,
            'mileage': 5000,
            'horsepower': 50,
            'repair_status': False,
            'notes': 'Test motorcycle',
            'fuel_type': 'Petrol',
            'engine_type': '4T'
        }
        form = MotorcycleForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_motorcycle_form_invalid(self):
        data = {
            'make': 'Honda',
            'model': 'CBR500',
            'production_date': '2019-05-01',
            'engine_displacement': 500,
            'mileage': 5000,
            'horsepower': 50,
            'repair_status': False,
            'notes': 'Test motorcycle',
            'fuel_type': 'Petrol',
            'engine_type': '3T'
        }
        form = MotorcycleForm(data=data)
        self.assertFalse(form.is_valid(), form.errors)

    def test_contact_form_valid(self):

        user = User.objects.create_user(email='test@email.com', password='12345')


        data = {
                'description': 'Test contact message',
        }

        form = ContactForm(data=data, user=user)


        self.assertTrue(form.is_valid(), form.errors)

    def test_contact_form_invalid(self):

        User = get_user_model()

        user = User.objects.create_user(email='test@email.com', password='12345')


        data = {'phone_number': '09883893832',
                'description': '',
        }

        form = ContactForm(data=data, user=user)


        self.assertFalse(form.is_valid(), form.errors)

    def test_employee_form_valid(self):

        data = {
            'company':'Motorheads',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 18,
            'hourly_wage': 40,
            'hours_weekly': 40,
            'hired_at': '2020-01-01'
        }

        form = EmployeeForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_employee_form_invalid(self):

        data = {
            'company':'Motorheads',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 12,
            'hourly_wage': 40,
            'hours_weekly': 40,
            'hired_at': '2020-01-01'
        }

        form = EmployeeForm(data=data)
        self.assertFalse(form.is_valid(), form.errors)