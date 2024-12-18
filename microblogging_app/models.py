from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     user_id = models.BigAutoField(primary_key=True)
#     nom = models.CharField(max_length=255)
#     prenom = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['nom', 'prenom']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_staff

#     def has_module_perms(self, app_label):
#         return self.is_staff


    
class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name','username']

    def __str__(self):
        return self.email

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, default=models.F('user__username'))
    # CustomUser est la primaryKey et la foreignKey est reliée à celle-ci 
    # La méthode cascade permet de supprimer tous les posts reliés à l'utilisateur, lorsque
    # l'utilisateur supprime son compte
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    # il s'agit d'indiquer ici la date du jour de façon auto
    update_at = models.DateField(null=True, blank=True)
    
   
    def __str__(self):
        return f'Post{self.post_id} by {self.user.email}'
    
    
class Profil(models.Model):
    profil_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, blank=False)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to ='images/')
    created_at = models.DateField(auto_now_add=True)  
    update_at = models.DateField(null=True, blank=True)
    
   
    def __str__(self):
        return f'Post{self.profil_id}'
   