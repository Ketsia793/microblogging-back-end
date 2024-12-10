from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import CustomUser, Profil 

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        Profil.objects.create(user=instance)
    
        
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    