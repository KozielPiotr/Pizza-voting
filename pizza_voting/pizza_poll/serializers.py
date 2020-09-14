"""
Serializers for pizza_poll application.
"""
from django.db.models import Count
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Pizza, Topping, Vote


class ToppingField(PrimaryKeyRelatedField):
    """Multichoice select field with possible toppings for pizza composition."""
    queryset = Topping.objects.all()


class ToppingSerializer(ModelSerializer):
    """Serializer for a Topping model."""

    class Meta:
        model = Topping
        fields = "__all__"


class VoteSerializer(ModelSerializer):
    """Serializer for a Vote model."""

    toppings = ToppingField(many=True, write_only=True)

    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ['pizza']

    def create(self, validated_data):
        toppings = validated_data["toppings"]

        pizza_query = Pizza.objects.annotate(count=Count("toppings")).filter(count=len(toppings))
        for topping in toppings:
            pizza_query = pizza_query.filter(toppings=topping)

        pizza = pizza_query.first()
        if not pizza:
            pizza = Pizza.objects.create()
            pizza.toppings.set(toppings)
        return Vote.objects.create(pizza=pizza)


class PizzaSerializer(ModelSerializer):
    """Serializer for a Pizza model."""

    toppings = ToppingSerializer(many=True, read_only=True)
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = "__all__"
