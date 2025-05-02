from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Station
        fields = ('id','station_name','region','distance')

class RouteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Route
        fields = ('id','person','station','car','date')
