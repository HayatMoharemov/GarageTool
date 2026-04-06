from django.test import TestCase
from accounts.models import GeneralUser, BusinessUser, IndividualUser
from garage.models import CarModel, MotorcycleModel
from employees.models import EmployeeModel
from contact.models import ContactModel
import datetime

class IntegrationModelsTestCase(TestCase):
    def setUp(self):

        self.business_user_email = "business@test.com"
        self.individual_user_email = "individual@test.com"

        # Създаваме GeneralUser
        self.business_user = GeneralUser.objects.create(
            email=self.business_user_email,
            type=GeneralUser.UserTypeChoices.BUSINESS,
            is_active=True
        )

        self.individual_user = GeneralUser.objects.create(
            email=self.individual_user_email,
            type=GeneralUser.UserTypeChoices.INDIVIDUAL,
            is_active=True
        )

        # Създаваме Car и Motorcycle
        self.car = CarModel.objects.create(
            owner=self.business_user,
            make="Audi",
            model="A4",
            production_date=datetime.date(2020, 1, 1),
            mileage=15000,
            engine_displacement=2.0,
            horsepower=190,
            fuel_type="PET",
            repair_status=False,
            notes="Test car"
        )

        self.motorcycle = MotorcycleModel.objects.create(
            owner=self.individual_user,
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

        self.employee = EmployeeModel.objects.create(
            company=self.business_user.businessuser,
            first_name="Ivan",
            last_name="Petrov",
            age=30,
            hourly_wage=15.50,
            hours_weekly=40,
            hired_at=datetime.date(2022, 5, 10),
            assigned_bikes=self.motorcycle
        )
        self.employee.assigned_cars.add(self.car)

        self.contact = ContactModel.objects.create(
            name=self.individual_user,
            company=self.business_user.businessuser,
            car=self.car,
            motorcycle=self.motorcycle,
            description="Integration test contact"
        )

        self.car.refresh_from_db()
        self.motorcycle.refresh_from_db()
        self.employee.refresh_from_db()


    def test_business_user_profile_created(self):
        self.assertTrue(BusinessUser.objects.filter(user=self.business_user).exists())
        bu_profile = BusinessUser.objects.get(user=self.business_user)
        self.assertEqual(bu_profile.user.email, self.business_user_email)

    def test_individual_user_profile_created(self):
        self.assertTrue(IndividualUser.objects.filter(user=self.individual_user).exists())
        iu_profile = IndividualUser.objects.get(user=self.individual_user)
        self.assertEqual(iu_profile.user.email, self.individual_user_email)


    def test_car_and_motorcycle_owner(self):
        self.assertEqual(self.car.owner, self.business_user)
        self.assertEqual(self.motorcycle.owner, self.individual_user)

    def test_employee_assignments(self):
        self.assertIn(self.car, self.employee.assigned_cars.all())
        self.assertEqual(self.employee.assigned_bikes, self.motorcycle)

    def test_contact_associations(self):
        self.assertEqual(self.contact.company, self.business_user.businessuser)
        self.assertEqual(self.contact.name, self.individual_user)
        self.assertEqual(self.contact.car, self.car)
        self.assertEqual(self.contact.motorcycle, self.motorcycle)