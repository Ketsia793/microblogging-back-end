from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    """Utilisateur personnalisé pour l'application."""
    user_id = models.BigAutoField(primary_key=True)