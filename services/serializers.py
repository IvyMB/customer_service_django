from rest_framework import serializers
from .models import Service
from clients.serializers import ClientSerializer


class ServiceSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Service
        fields = '__all__'
