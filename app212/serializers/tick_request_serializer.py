from rest_framework import serializers

from app212.models import Tick


class TickRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tick
        fields = ['payload']

    payload = serializers.JSONField(required=False, allow_null=True)
