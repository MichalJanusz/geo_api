from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass


class GeolocData(models.Model):
    ip = models.CharField(max_length=64, unique=True)
    ip_type = models.CharField(max_length=4)
    continent_code = models.CharField(max_length=2)
    continent_name = models.CharField(max_length=32)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=64)
    region_code = models.CharField(max_length=2)
    region_name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zip = models.CharField(max_length=16)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
