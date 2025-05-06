from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers, models, api
from .authentication import login_view

UserList = api.UserList()
UserDetail = api.UserDetail()
StationList = api.StationList()
StationDetail = api.StationDetail()
RouteList = api.RouteList()
RouteDetail = api.RouteDetail()

login_view = login_view
