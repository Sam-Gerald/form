from django.contrib import admin
from django.urls import path, include
# from django.config import settings
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]