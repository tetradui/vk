from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.create_activation_code()
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        user = self._create_user(email, password, **extra_fields)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    pro_photo = models.ImageField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    activation_code = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='0123456789')
        self.activation_code = code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте поля профиля
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()