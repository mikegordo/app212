from django.conf import settings
from django.db import models


class Tick(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    created = models.DateTimeField('Created', auto_now_add=True)
    payload = models.JSONField('Payload', null=True, blank=True)

    class Meta:
        verbose_name = 'Tick'
        verbose_name_plural = 'Ticks'
