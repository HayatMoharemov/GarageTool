# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
#
# import os
# import sys
#
# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GarageTool.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)
#
#
# if __name__ == '__main__':
#     main()
#
# from catalogue.models import ServiceModel, PartModel
# from garage.models import MotorcycleModel, CarModel
# from employees.models import EmployeeModel
# import datetime
#
# # -------------------- CARS --------------------
# Car_1 = CarModel(
#     make="Audi",
#     model="A4",
#     production_date=datetime.date(2018, 5, 20),
#     mileage=25000,
#     engine_displacement=2.0,
#     horsepower=190,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Needs a turbo check"
# )
# Car_1.save()
#
# Car_2 = CarModel(
#     make="BMW",
#     model="320i",
#     production_date=datetime.date(2019, 3, 15),
#     mileage=18000,
#     engine_displacement=2.0,
#     horsepower=184,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Knocks from the right side front"
# )
# Car_2.save()
#
# Car_3 = CarModel(
#     make="Mercedes",
#     model="C200",
#     production_date=datetime.date(2017, 8, 10),
#     mileage=40000,
#     engine_displacement=1.8,
#     horsepower=156,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Leaks oil"
# )
# Car_3.save()
#
# Car_4 = CarModel(
#     make="Toyota",
#     model="Corolla",
#     production_date=datetime.date(2020, 1, 5),
#     mileage=15000,
#     engine_displacement=1.6,
#     horsepower=132,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Transmission oil needed"
# )
# Car_4.save()
#
# Car_5 = CarModel(
#     make="Honda",
#     model="Civic",
#     production_date=datetime.date(2019, 7, 12),
#     mileage=22000,
#     engine_displacement=1.5,
#     horsepower=174,
#     fuel_type="PET",
#     repair_status=False,
#     notes="All round vehicle check"
# )
# Car_5.save()
#
# Car_6 = CarModel(
#     make="Volkswagen",
#     model="Passat",
#     production_date=datetime.date(2016, 11, 30),
#     mileage=50000,
#     engine_displacement=2.0,
#     horsepower=170,
#     fuel_type="DIESEL",
#     repair_status=False,
#     notes="Needs new bushings on the front axle"
# )
# Car_6.save()
#
# Car_7 = CarModel(
#     make="Ford",
#     model="Focus",
#     production_date=datetime.date(2018, 4, 22),
#     mileage=30000,
#     engine_displacement=1.5,
#     horsepower=150,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Brakes back"
# )
# Car_7.save()
#
# Car_8 = CarModel(
#     make="Nissan",
#     model="Altima",
#     production_date=datetime.date(2020, 6, 18),
#     mileage=12000,
#     engine_displacement=2.5,
#     horsepower=188,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Brakes front"
# )
# Car_8.save()
#
# Car_9 = CarModel(
#     make="Hyundai",
#     model="Elantra",
#     production_date=datetime.date(2019, 9, 9),
#     mileage=20000,
#     engine_displacement=2.0,
#     horsepower=147,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Needs full service"
# )
# Car_9.save()
#
# Car_10 = CarModel(
#     make="Kia",
#     model="Optima",
#     production_date=datetime.date(2017, 2, 27),
#     mileage=35000,
#     engine_displacement=2.4,
#     horsepower=185,
#     fuel_type="PET",
#     repair_status=False,
#     notes="Requires service soon"
# )
# Car_10.save()
#
#
# # -------------------- MOTORCYCLES --------------------
# Moto_1 = MotorcycleModel(
#     make="Yamaha",
#     model="R1",
#     production_date=datetime.date(2020, 3, 12),
#     mileage=4000,
#     engine_displacement=998,
#     horsepower=200,
#     engine_type="4T",
#     repair_status=False,
#     notes="Filters and transmission oil"
# )
# Moto_1.save()
#
# Moto_2 = MotorcycleModel(
#     make="Honda",
#     model="CBR600RR",
#     production_date=datetime.date(2019, 6, 5),
#     mileage=7000,
#     engine_displacement=599,
#     horsepower=120,
#     engine_type="4T",
#     repair_status=False,
#     notes="Brake pads and oil service"
# )
# Moto_2.save()
#
# Moto_3 = MotorcycleModel(
#     make="Kawasaki",
#     model="Ninja ZX-6R",
#     production_date=datetime.date(2018, 9, 10),
#     mileage=10000,
#     engine_displacement=636,
#     horsepower=130,
#     engine_type="4T",
#     repair_status=False,
#     notes="Needs new axle bearings"
# )
# Moto_3.save()
#
# Moto_4 = MotorcycleModel(
#     make="Suzuki",
#     model="GSX-R750",
#     production_date=datetime.date(2017, 11, 20),
#     mileage=12000,
#     engine_displacement=750,
#     horsepower=148,
#     engine_type="4T",
#     repair_status=False,
#     notes="Needs service"
# )
# Moto_4.save()
#
# Moto_5 = MotorcycleModel(
#     make="Ducati",
#     model="Panigale V2",
#     production_date=datetime.date(2021, 1, 15),
#     mileage=3000,
#     engine_displacement=955,
#     horsepower=155,
#     engine_type="4T",
#     repair_status=False,
#     notes="Need new alternator"
# )
# Moto_5.save()
#
# Moto_6 = MotorcycleModel(
#     make="BMW",
#     model="S1000RR",
#     production_date=datetime.date(2020, 5, 22),
#     mileage=3500,
#     engine_displacement=999,
#     horsepower=205,
#     engine_type="4T",
#     repair_status=False,
#     notes="Need new tires"
# )
# Moto_6.save()
#
# Moto_7 = MotorcycleModel(
#     make="KTM",
#     model="RC390",
#     production_date=datetime.date(2019, 8, 3),
#     mileage=6000,
#     engine_displacement=373,
#     horsepower=44,
#     engine_type="4T",
#     repair_status=False,
#     notes="New shock front"
# )
# Moto_7.save()
#
# Moto_8 = MotorcycleModel(
#     make="Aprilia",
#     model="RS660",
#     production_date=datetime.date(2021, 4, 18),
#     mileage=2000,
#     engine_displacement=659,
#     horsepower=100,
#     engine_type="4T",
#     repair_status=False,
#     notes="New shock back"
# )
# Moto_8.save()
#
# Moto_9 = MotorcycleModel(
#     make="Yamaha",
#     model="MT-07",
#     production_date=datetime.date(2018, 2, 12),
#     mileage=9000,
#     engine_displacement=689,
#     horsepower=74,
#     engine_type="4T",
#     repair_status=False,
#     notes="New brakes needed"
# )
# Moto_9.save()
#
# Moto_10 = MotorcycleModel(
#     make="KTM",
#     model="Duke 390",
#     production_date=datetime.date(2017, 12, 25),
#     mileage=11000,
#     engine_displacement=373,
#     horsepower=44,
#     engine_type="4T",
#     repair_status=False,
#     notes="Oil change needed"
# )
# Moto_10.save()
#
#
# # -------------------- EMPLOYEES --------------------
# employees_data = [
#     {
#         "first_name": "Ivan",
#         "last_name": "Petrov",
#         "age": 28,
#         "hourly_wage": 15.50,
#         "hours_weekly": 40,
#         "hired_at": datetime.date(2022, 5, 10),
#     },
#     {
#         "first_name": "Georgi",
#         "last_name": "Dimitrov",
#         "age": 35,
#         "hourly_wage": 18.75,
#         "hours_weekly": 42,
#         "hired_at": datetime.date(2021, 3, 15),
#     },
#     {
#         "first_name": "Nikolay",
#         "last_name": "Ivanov",
#         "age": 30,
#         "hourly_wage": 17.00,
#         "hours_weekly": 38,
#         "hired_at": datetime.date(2023, 1, 20),
#     },
#     {
#         "first_name": "Petar",
#         "last_name": "Stoyanov",
#         "age": 41,
#         "hourly_wage": 20.00,
#         "hours_weekly": 45,
#         "hired_at": datetime.date(2020, 7, 1),
#     },
#     {
#         "first_name": "Dimitar",
#         "last_name": "Kolev",
#         "age": 26,
#         "hourly_wage": 14.25,
#         "hours_weekly": 40,
#         "hired_at": datetime.date(2024, 2, 12),
#     },
#     {
#         "first_name": "Hristo",
#         "last_name": "Georgiev",
#         "age": 33,
#         "hourly_wage": 19.10,
#         "hours_weekly": 39,
#         "hired_at": datetime.date(2019, 11, 5),
#     },
#     {
#         "first_name": "Martin",
#         "last_name": "Todorov",
#         "age": 29,
#         "hourly_wage": 16.80,
#         "hours_weekly": 41,
#         "hired_at": datetime.date(2022, 9, 18),
#     },
#     {
#         "first_name": "Stefan",
#         "last_name": "Nikolov",
#         "age": 37,
#         "hourly_wage": 21.30,
#         "hours_weekly": 44,
#         "hired_at": datetime.date(2018, 4, 22),
#     },
# ]
#
# for data in employees_data:
#     EmployeeModel.objects.create(**data)
#
#
# #-------------------SERVICES ----------------------
# services_data = [
#     {"title": "Oil Change", "price": 80.00, "description": "Engine oil replacement with standard oil."},
#     {"title": "Oil Filter Replacement", "price": 25.00, "description": "Replacement of engine oil filter."},
#     {"title": "Air Filter Replacement", "price": 30.00, "description": "Replacement of engine air filter."},
#     {"title": "Cabin Filter Replacement", "price": 35.00, "description": "Replacement of cabin pollen filter."},
#     {"title": "Brake Pads Replacement", "price": 120.00, "description": "Replacement of front or rear brake pads."},
#     {"title": "Brake Discs Replacement", "price": 220.00, "description": "Replacement of brake discs."},
#     {"title": "AC Recharge", "price": 150.00, "description": "Air conditioning system recharge with freon."},
#     {"title": "Battery Replacement", "price": 60.00, "description": "Car battery replacement service."},
#     {"title": "Timing Belt Replacement", "price": 450.00, "description": "Timing belt kit replacement."},
#     {"title": "Wheel Alignment", "price": 70.00, "description": "Wheel alignment and adjustment."},
# ]
#
# for data in services_data:
#     ServiceModel.objects.create(**data)
#
#
# #-------------------PARTS ----------------------
# parts_data = [
#     {"title": "Engine Oil 5W-30", "price": 45.00, "manufacturer": "Castrol"},
#     {"title": "Oil Filter", "price": 12.50, "manufacturer": "Bosch"},
#     {"title": "Air Filter", "price": 18.00, "manufacturer": "Mann"},
#     {"title": "Cabin Filter", "price": 22.00, "manufacturer": "Mahle"},
#     {"title": "Brake Pads Front", "price": 95.00, "manufacturer": "Brembo"},
#     {"title": "Brake Pads Rear", "price": 85.00, "manufacturer": "ATE"},
#     {"title": "Brake Discs Front", "price": 180.00, "manufacturer": "Brembo"},
#     {"title": "Brake Discs Rear", "price": 160.00, "manufacturer": "ATE"},
#     {"title": "Car Battery 74Ah", "price": 210.00, "manufacturer": "Varta"},
#     {"title": "Alternator", "price": 350.00, "manufacturer": "Bosch"},
#     {"title": "Starter Motor", "price": 320.00, "manufacturer": "Valeo"},
#     {"title": "Timing Belt Kit", "price": 270.00, "manufacturer": "Gates"},
#     {"title": "Water Pump", "price": 120.00, "manufacturer": "SKF"},
#     {"title": "Clutch Kit", "price": 480.00, "manufacturer": "LUK"},
#     {"title": "Shock Absorber Front", "price": 150.00, "manufacturer": "KYB"},
#     {"title": "Shock Absorber Rear", "price": 130.00, "manufacturer": "Monroe"},
#     {"title": "Spark Plug", "price": 15.00, "manufacturer": "NGK"},
#     {"title": "Ignition Coil", "price": 95.00, "manufacturer": "Bosch"},
#     {"title": "Fuel Pump", "price": 260.00, "manufacturer": "Pierburg"},
#     {"title": "Radiator", "price": 340.00, "manufacturer": "Nissens"},
#     {"title": "Thermostat", "price": 40.00, "manufacturer": "Mahle"},
#     {"title": "EGR Valve", "price": 290.00, "manufacturer": "Pierburg"},
#     {"title": "Lambda Sensor", "price": 180.00, "manufacturer": "Bosch"},
#     {"title": "Drive Belt", "price": 55.00, "manufacturer": "Continental"},
#     {"title": "Wheel Bearing", "price": 110.00, "manufacturer": "SKF"},
#     {"title": "Control Arm", "price": 145.00, "manufacturer": "Lemforder"},
#     {"title": "Tie Rod End", "price": 60.00, "manufacturer": "TRW"},
#     {"title": "CV Joint", "price": 190.00, "manufacturer": "GKN"},
#     {"title": "Headlight Bulb H7", "price": 20.00, "manufacturer": "Philips"},
#     {"title": "Windshield Wipers", "price": 35.00, "manufacturer": "Bosch"},
# ]
#
# for data in parts_data:
#     PartModel.objects.create(**data)