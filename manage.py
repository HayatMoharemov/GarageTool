#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GarageTool.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# from catalogue.models import ServiceModel, PartModel
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