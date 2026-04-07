from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from GarageTool import settings
from accounts.models import BusinessUser, IndividualUser

UserModel = get_user_model()
'''
Signal that automatically creates a profile for a new GeneralUser.
    - Triggered after a GeneralUser instance is created.
    - If the user is a business, a BusinessUser profile is created.
    - If the user is an individual, an IndividualUser profile is created.
'''

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_business:
            BusinessUser.objects.create(
                user=instance
            )
        elif instance.is_individual:
            IndividualUser.objects.create(
                user=instance
            )


'''
Signal that automatically creates two User Groups in Django Admin upon making the first migrations.
    -Editor Group (allowed to edit vehicles)
    -Admin Group (full permissions)
'''

@receiver(post_migrate)
def create_default_user_groups(sender, **kwargs):

    if sender.name != 'accounts':
        return

    editor_group, created = Group.objects.get_or_create(name='Editor')

    try:
        CarModel = apps.get_model('garage', 'CarModel')
        MotorcycleModel = apps.get_model('garage', 'MotorcycleModel')

        car_permission = Permission.objects.get(content_type__app_label='garage', codename='change_carmodel')
        moto_permission = Permission.objects.get(content_type__app_label='garage', codename='change_motorcyclemodel')

        editor_group.permissions.set([car_permission, moto_permission])
    except (LookupError, Permission.DoesNotExist):
        pass

    admin_group, created = Group.objects.get_or_create(name='Admin')
    all_perms = Permission.objects.all()
    admin_group.permissions.set(all_perms)

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_business:

            BusinessUser.objects.create(
                user=instance,
                company_name='Default Company',
                tax_number='0000000000'
            )
        elif instance.is_individual:
            IndividualUser.objects.create(user=instance)