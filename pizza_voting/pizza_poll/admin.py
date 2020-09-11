"""Django admin site configuration."""

from django.contrib import admin

from .models import Pizza, Topping, Vote


admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Vote)
