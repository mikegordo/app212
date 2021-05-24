from rest_framework import serializers

from app212.models import Tick


class TickResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tick
        fields = ['id', 'payload', 'created']
