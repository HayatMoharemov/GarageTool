import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from garage.models import CarModel, MotorcycleModel

User = get_user_model()

class GarageViewsTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(email='business@email.com', password='12345', type='BU')
        self.client.login(email='business@email.com', password='12345')

        self.car = CarModel.objects.create(
            owner=self.user,
            make="Toyota",
            model="Corolla",
            production_date=datetime.date(2020, 1, 1),
            mileage=15000,
            engine_displacement=2.0,
            horsepower=190,
            fuel_type="PET",
            repair_status=False,
            notes="Test car"
        )

        self.motorcycle = MotorcycleModel.objects.create(
            owner=self.user,
            make="Yamaha",
            model="R1",
            production_date=datetime.date(2021, 5, 1),
            mileage=3000,
            engine_displacement=998,
            horsepower=200,
            engine_type="4T",
            repair_status=False,
            notes="Test motorcycle"
        )

    def test_view_garage(self):
        url = reverse('garage:view_garage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')
        self.assertContains(response, 'Yamaha')

    def test_add_car_view(self):
        url = reverse('garage:add_car')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_add_bike_view(self):
        url = reverse('garage:add_bike')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_vehicle_detail_view_car(self):
        url = reverse('garage:vehicle_detail', kwargs={'vehicle_slug': self.car.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')

    def test_vehicle_detail_view_motorcycle(self):
        url = reverse('garage:vehicle_detail', kwargs={'vehicle_slug': self.motorcycle.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Yamaha')

    def test_vehicle_edit_view_car(self):
        url = reverse('garage:vehicle_edit', kwargs={'vehicle_slug': self.car.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_vehicle_edit_view_motorcycle(self):
        url = reverse('garage:vehicle_edit', kwargs={'vehicle_slug': self.motorcycle.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_delete_vehicle_view_car(self):
        url = reverse('garage:vehicle_delete', kwargs={'vehicle_slug': self.car.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure')

    def test_delete_vehicle_view_motorcycle(self):
        url = reverse('garage:vehicle_delete', kwargs={'vehicle_slug': self.motorcycle.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure')