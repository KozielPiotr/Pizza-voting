"""Models for pizza_poll application."""

from django.db import models


class Pizza(models.Model):
    """
    Kinds of pizzas with their toppings.
    Has many to many relationship with 'Topping' table:
    - one pizza can have many toppings;
    - one topping can be an ingredient for many pizzas.
    Is a part of one to many relationship with 'Vote'table:
    - a single vote may be cast for only one pizza;
    - a single pizza can collect multiple votes.
    """

    toppings = models.ManyToManyField("Topping", related_name="pizzas", blank=True)

    def __str__(self):
        return "Pizza {}".format(self.toppings)


class Topping(models.Model):
    """
    List of toppings available for pizzas.
    Is a part of many to many relationship with 'Pizza' table:
    - one pizza can have many toppings;
    - one topping can be an ingredient for many pizzas.
    """

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "Topping {}".format(self.name)


class Vote(models.Model):
    """
    Votes for the pizza.
    Has one to many relationship with 'Pizza'table:
    - a single vote may be cast for only one pizza;
    - a single pizza can collect multiple votes;
    - deleting Pizza object should also delete it's votes.
    """

    timestamp = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(
        Pizza, on_delete=models.CASCADE, related_name="votes", null=False, blank=False
    )

    def __str__(self):
        return "A vote for {} casted {}".format(self.pizza, self.timestamp)
