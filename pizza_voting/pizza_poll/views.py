# pylint: disable=too-many-ancestors
"""Views for pizza_poll application."""

from django.db.models import Count, Sum

from rest_framework import mixins
from rest_framework.viewsets import (
    GenericViewSet,
    ReadOnlyModelViewSet,
)

from .models import Pizza, Topping, Vote
from .serializers import PizzaSerializer, ToppingSerializer, VoteSerializer


class ListCreateModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    pass


class PizzaViewSet(ReadOnlyModelViewSet):
    """Api to view or edit a Pizza object."""

    queryset = (
        Pizza.objects.all()
        .annotate(votes_count=Count("votes"))
        .order_by("-votes_count")
    )
    serializer_class = PizzaSerializer


class ToppingViewSet(ListCreateModelViewSet):
    """Api to view or edit a Topping object."""

    queryset = (
        Topping.objects.all()
        .annotate(votes_count=Sum("pizzas__votes"))
        .order_by("-votes_count")
    )
    serializer_class = ToppingSerializer


class VoteViewSet(ListCreateModelViewSet):
    """Api to view or edit a Vote object."""

    queryset = Vote.objects.all().order_by("-timestamp")
    serializer_class = VoteSerializer
