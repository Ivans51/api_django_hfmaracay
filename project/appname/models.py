from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    AREA_CHOICE = (
        ('Programación', 'Programación'),
        ('Diseño', 'Diseño'),
        ('Marketing', 'Marketing'),
        ('Finanzas', 'Finanzas'),
        ('Emprendimiento', 'Emprendimiento'),
    )
    LEVEL_CHOICE = (
        ('Estudiante', 'Estudiante'),
        ('Profesional', 'Profesional'),
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    address = models.CharField(_('address'), max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)
    area = models.CharField(max_length=30, choices=AREA_CHOICE)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICE)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
