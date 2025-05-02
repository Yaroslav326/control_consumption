from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers, models

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class StationList(generics.ListAPIView):
    queryset = models.Station.objects.all()
    serializer_class = serializers.StationSerializer


class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Station.objects.all()
    serializer_class = serializers.StationSerializer


class RouteList(generics.ListAPIView):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
