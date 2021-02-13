from rest_framework import serializers
from my_api.models import GeolocData


class GeolocDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeolocData
        fields = '__all__'
