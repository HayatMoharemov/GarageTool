from django.db.models.signals import post_save
from django.dispatch import receiver

from GarageTool import settings
from accounts.models import BusinessUser, IndividualUser

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