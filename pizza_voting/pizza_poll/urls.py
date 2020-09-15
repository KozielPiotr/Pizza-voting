"""URL configuration for pizza_poll application."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PizzaViewSet, ToppingViewSet, VoteViewSet

router = DefaultRouter()
router.register("pizzas", PizzaViewSet, basename="pizza")
router.register("toppings", ToppingViewSet, basename="topping")
router.register("votes", VoteViewSet, basename="vote")

urlpatterns = [
    path("", include(router.urls)),
]
