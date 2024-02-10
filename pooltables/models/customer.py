from django.db import models
from PIL import Image
from django.utils.translation import gettext as _
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin,  Group, Permission
from django.conf import settings
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, blank=False, default='')
    password = models.CharField(max_length=255)
    profile_pic = models.ImageField(
    verbose_name='Profile Picture',
    upload_to='images/',
    default='images/avatar.jpg',
    blank=True
    )
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    # Use email as the unique identifier for authentications

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    @staticmethod
    def get_user_by_email(email):
        try:
            return CustomUser.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if CustomUser.objects.filter(email = self.email):
            return True
        return False
# Save it again and override the larger image

    @property
    def get_image(self):
        return self.image.url if self.image else static('avatar.jpg')


        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) 
