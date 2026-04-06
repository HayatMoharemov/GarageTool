import asyncio

from asgiref.sync import sync_to_async

from .models import CarModel, MotorcycleModel

async def check_not_repaired_vehicles():
    while True:

        not_repaired_cars = await sync_to_async(lambda: list(CarModel.objects.filter(repair_status=False)))()
        not_repaired_bikes = await sync_to_async(lambda: list(MotorcycleModel.objects.filter(repair_status=False)))()

        if not_repaired_cars:
            print("Cars that are still not repaired:")
            for car in not_repaired_cars:
                print (f" - {car.make} {car.model} with ID {car.id}")
        else:
            print(f"Everything looks good!\nYou don't have unrepaired cars currently")

        if not_repaired_bikes:
            print("Motorcycles that are still not repaired:")
            for bike in not_repaired_bikes:
                print(f"- {bike.make} {bike.model} with ID {bike.id}")
        else:
            print("Everything looks good!\nYou don't have unrepaired motorcycles currently")

        await asyncio.sleep(3600)