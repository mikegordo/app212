from django.contrib.auth.models import AbstractUser
from django.db import models

from .base_model import BaseModel


class User(BaseModel, AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    groups = None

    is_active = models.BooleanField(
        'Active',
        default=True,
    )

    is_deleted = models.BooleanField(
        'Deleted',
        default=False,
    )
