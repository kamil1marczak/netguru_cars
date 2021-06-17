import factory

from car_api.cars.models import Car, Rating
from factory import Faker
from factory.django import DjangoModelFactory


class CarFactory(DjangoModelFactory):
    make = Faker("company")
    model = Faker("company")

    class Meta:
        model = Car
        django_get_or_create = [
            "make",
            "model",
        ]


class RateFactory(DjangoModelFactory):
    rating_value = Faker("random_int")
    car = factory.SubFactory(CarFactory)

    class Meta:
        model = Rating
        django_get_or_create = [
            "rating_value",
        ]
