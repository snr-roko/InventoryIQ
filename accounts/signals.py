from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """
    This signal function is used to automatically create a profile when a user is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
