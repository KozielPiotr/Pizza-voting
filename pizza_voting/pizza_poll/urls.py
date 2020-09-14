"""URL configuration for pizza_poll application."""

from django.urls import include, path
# from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.routers import SimpleRouter

from .views import PizzaViewSet, ToppingViewSet, VoteViewSet

router = SimpleRouter()
router.register("pizzas", PizzaViewSet, basename="pizzas")
router.register("toppings", ToppingViewSet, basename="toppings")
router.register("votes", VoteViewSet, basename="votes")

# pizza_router = NestedSimpleRouter(router, "pizzas", lookup="pizza")

urlpatterns = [
    path("", include(router.urls)),
    # path("", include(pizza_router.urls))
]
