"""
URL configuration for the hotel_management project.

This file defines the URL routing for the project, including the admin site
and the URL patterns for the `hotel_app` application.
"""

from django.contrib import admin
from django.urls import path, include  # 'include' is used to include app-level URLs

urlpatterns = [
    path("admin/", admin.site.urls),  # URL for admin panel
    path("rooms/", include("hotel_app.urls")),  # Include URLs from the hotel_app
]
