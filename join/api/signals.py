from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from ..models import Profile, Color

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        default_color = Color.objects.first()  # Wähle eine Standardfarbe aus
        avatar = ''
        if instance.first_name:
            avatar += instance.first_name[0].upper()
        if instance.last_name:
            avatar += instance.last_name[0].upper()
        Profile.objects.create(user=instance, color=default_color, avatar=avatar)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()