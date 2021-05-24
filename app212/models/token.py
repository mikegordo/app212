import binascii
import os

from django.conf import settings
from django.db import models
from django.utils import timezone


class Token(models.Model):
    key = models.CharField('Key', max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField('Created', auto_now_add=True)
    last_used = models.DateTimeField('Last used', auto_now=True)
    times_used = models.IntegerField('Times used', default=0, null=False)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def update_last_used(self):
        self.last_used = timezone.localtime()

    def update_times_used(self):
        self.times_used += 1

    def __str__(self):
        return self.key
