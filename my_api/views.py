from django.shortcuts import render
from my_api.models import GeolocData
from my_api.serializers import GeolocDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json


# Create your views here.

class GeolocDataList(APIView):

    def get(self, request, format=None):
        geo_data = GeolocData.objects.all()
        serializer = GeolocDataSerializer(geo_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeolocDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeolocDataDetails(APIView):

    def get_object(self, ip):
        try:
            return GeolocData.objects.get(ip=ip)
        except GeolocData.DoesNotExist:
            r = requests.get(f'http://api.ipstack.com/{ip}?access_key=d7b132f2f6577bc9e75e44111769d714&fields=ip,'
                             f'type,continent_code,continent_name,country_code,country_name,region_code,region_name,'
                             f'city,zip,latitude,longitude')
            json_data = json.loads(r.content)
            return GeolocData.objects.create(
                ip=json_data['ip'], ip_type=json_data['type'],
                continent_code=json_data['continent_code'], continent_name=json_data['continent_name'],
                country_code=json_data['country_code'], country_name=json_data['country_name'],
                region_code=json_data['region_code'], region_name=json_data['region_name'], city=json_data['city'],
                zip=json_data['zip'], latitude=json_data['latitude'], longitude=json_data['longitude'])

    def get(self, request, ip, format=None):
        geo_data = self.get_object(ip)
        serializer = GeolocDataSerializer(geo_data)
        return Response(serializer.data)

    def put(self, request, ip, format=None):
        geo_data = self.get_object(ip)
        serializer = GeolocDataSerializer(geo_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ip, format=None):
        geo_data = self.get_object(ip)
        geo_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

