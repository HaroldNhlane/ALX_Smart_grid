# grid/serializers.py

from rest_framework import serializers
from .models import Device, SensorData, Alert

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

# Serializer for the SensorData model
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

# Serializer for the Alert model
class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'