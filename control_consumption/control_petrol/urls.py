from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('stations/', views.StationList.as_view()),
    path('stations/<int:pk>/', views.StationDetail.as_view()),
    path('routes/', views.RouteList.as_view()),
    path('routes/<int:pk>/', views.RouteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
