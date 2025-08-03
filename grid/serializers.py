from rest_framework import serializers
from .models import SomeModel

class SomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = '__all__'
