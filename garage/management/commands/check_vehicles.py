import asyncio
from django.core.management import BaseCommand
from garage.tasks import check_not_repaired_vehicles


class Command(BaseCommand):
    help = 'Async task: Checks for unrepaired cars and motorcycles every 1 hour and prints them'

    def handle(self, *args, **options):
        asyncio.run(check_not_repaired_vehicles())