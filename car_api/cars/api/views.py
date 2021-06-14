from django.db.models import Count
from rest_framework import viewsets

from car_api.cars.models import Car, Rating
from car_api.cars.api.serializers import (
    CarSerializer,
    RatingSerializer,
    PopularCarSerializer,
)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class PopularCarViewSet(viewsets.ModelViewSet):
    queryset = (
        Car.objects.all()
        .annotate(num_ratings=Count("ratings"))
        .order_by("-num_ratings")
    )
    serializer_class = PopularCarSerializer
