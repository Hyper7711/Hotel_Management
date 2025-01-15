"""
URL configuration for the hotel_app.

This file defines the URL patterns for the hotel_app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("rooms/", views.room_list, name="room_list"),
]
