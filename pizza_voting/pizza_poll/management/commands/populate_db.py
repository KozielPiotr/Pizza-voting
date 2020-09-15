"""Custom command to prepopulated a database."""

from django.core.management.base import BaseCommand
from pizza_poll.models import Topping, Vote, Pizza


class Command(BaseCommand):
    help = "Command prepopulates database with some sample data. It creates sample toppings and votes."

    toppings = [
        "ham",
        "cheese",
        "broccoli",
        "oregano",
        "mushrooms",
        "olives",
        "spinach",
    ]

    def _create_toppings(self, toppings):
        """Creates some Topping objects."""
        for topping in toppings:
            Topping.objects.create(name=topping)

    def _create_votes(self, toppings):
        """Creates some Vote and Pizza objects."""
        pizza = Pizza.objects.create()
        pizza.toppings.set(
            [
                Topping.objects.get(name=toppings[0]),
                Topping.objects.get(name=toppings[2]),
            ]
        )
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)

        pizza = Pizza.objects.create()
        pizza.toppings.set(
            [
                Topping.objects.get(name=toppings[1]),
                Topping.objects.get(name=toppings[0]),
            ]
        )
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)

        pizza = Pizza.objects.create()
        pizza.toppings.set(
            [
                Topping.objects.get(name=toppings[3]),
                Topping.objects.get(name=toppings[4]),
            ]
        )
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)

        pizza = Pizza.objects.create()
        pizza.toppings.set(
            [
                Topping.objects.get(name=toppings[-1]),
                Topping.objects.get(name=toppings[0]),
            ]
        )
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)

        pizza = Pizza.objects.create()
        pizza.toppings.set(
            [
                Topping.objects.get(name=toppings[3]),
                Topping.objects.get(name=toppings[-1]),
            ]
        )
        Vote.objects.create(pizza=pizza)
        Vote.objects.create(pizza=pizza)

    def handle(self, *args, **options):
        self._create_toppings(toppings=self.toppings)
        self._create_votes(toppings=self.toppings)
