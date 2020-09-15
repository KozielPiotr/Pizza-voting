"""
Serializers for pizza_poll application.
"""

from django.db.models import Count
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    SerializerMethodField,
    SlugRelatedField,
)

from .models import Pizza, Topping, Vote


class ToppingsField(SlugRelatedField):
    """Multiple choice select field with possible toppings for pizza composition."""

    queryset = Topping.objects.all()

    def __init__(self, **kwargs):
        super().__init__(slug_field="name", **kwargs)


class ToppingSerializer(HyperlinkedModelSerializer):
    """Serializer for a Topping model."""

    votes_count = SerializerMethodField()

    class Meta:
        model = Topping
        exclude = ["url"]

    def get_votes_count(self, obj):
        """Counts amount of votes casted for pizza with given topping."""
        return obj.pizzas.aggregate(Count("votes"))["votes__count"]


class VoteSerializer(HyperlinkedModelSerializer):
    """Serializer for a Vote model."""

    toppings = ToppingsField(many=True, write_only=True)

    class Meta:
        model = Vote
        exclude = ["url"]
        read_only_fields = ["pizza"]

    def create(self, validated_data):
        """
        Checks if given composition exist. If it is, a Vote object related to Pizza object is created.
        If composition doesn't exists it is created with related Vote object.
        """
        toppings = validated_data["toppings"]

        pizza_query = Pizza.objects.annotate(count=Count("toppings")).filter(
            count=len(toppings)
        )
        for topping in toppings:
            pizza_query = pizza_query.filter(toppings=topping)

        pizza = pizza_query.first()
        if not pizza:
            pizza = Pizza.objects.create()
            pizza.toppings.set(toppings)

        return Vote.objects.create(pizza=pizza)


class PizzaSerializer(HyperlinkedModelSerializer):
    """Serializer for a Pizza model."""

    toppings = ToppingsField(many=True)
    votes_count = SerializerMethodField()

    def get_votes_count(self, obj):
        """Counts amount of votes casted for pizza composition."""
        return obj.votes.count()

    class Meta:
        model = Pizza
        fields = "__all__"
