"""pizza_voting URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import APIRootView


api_root_views = {
    "pizzas": "pizzas-list",
    "toppings": "toppings-list",
    "votes": "votes-list",
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", APIRootView.as_view(api_root_dict=api_root_views), name="api-root"),
    path("api/", include("pizza_poll.urls")),
]
