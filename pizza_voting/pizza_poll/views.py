# pylint: disable=too-many-ancestors
"""Views for pizza_poll application."""

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import Pizza, Topping, Vote
from .serializers import PizzaSerializer, ToppingSerializer, VoteSerializer


class PizzaViewSet(ModelViewSet):
    """Api to view or edit a Pizza object."""

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class ToppingViewSet(ModelViewSet):
    """Api to view or edit a Topping object."""

    queryset = Topping.objects.all().order_by("name")
    serializer_class = ToppingSerializer


class VoteViewSet(ModelViewSet):
    """Api to view or edit a Vote object."""

    queryset = Vote.objects.all().order_by("-timestamp")
    serializer_class = VoteSerializer


class RelatedVoteViewSet(ModelViewSet):
    """
    View of Vote object(s) related to the Pizza object.
    This view is nested in Pizza detail or list endpoints.
    """

    serializer_class = VoteSerializer

    # def get_queryset(self):
    #     """Query of all Vote objects being related to the given Pizza."""
    #
    #     return Vote.objects.filter(pizza=self.get_pizza())

    def get_pizza(self):
        """Gets queryset for Pizza objects with given pk."""

        query = Pizza.objects.filter(
            pk=self.kwargs["pizza_pk"]
        )
        return get_object_or_404(query)
