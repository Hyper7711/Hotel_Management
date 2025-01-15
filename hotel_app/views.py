"""
Views for the hotel_app.

This file contains the views for handling HTTP requests for the hotel management system.
"""

from django.http import HttpResponse


def room_list():  # noqa: ARG001
    """Handle requests to the /rooms/ URL and return a list of rooms."""
    # Suppressed unused argument warning with `# noqa: ARG001`
    return HttpResponse("This is the list of rooms.")
