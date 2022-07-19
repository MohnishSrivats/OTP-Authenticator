from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.otpAuth),
    path('users/', views.usersList),
]