from django.contrib import admin
from car_api.cars.models import Car, Rating


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ["make", "model"]
    list_display = ["id", "make", "model", "avg_rating", "rates_number"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    fields = ["car", "rating_value"]
    list_display = ["id", "car", "rating_value"]
