"""
Pizza_voting URL Configuration.
Admin url is omitted, as it makes completely no use with this structure of the project.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("pizza_poll.urls")),
]
