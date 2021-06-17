import pytest
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory

from car_api.users.models import User
from car_api.cars.models import Car, Rating

from car_api.cars.api.views import (
    CarViewSet,
    RateViewSet,
)

from car_api.cars.api.serializers import (
    CarSerializer,
    RatingSerializer,
)


@pytest.mark.django_db
def test_car_list():
    assert reverse("api:car-list") == "/api/cars/"
    assert resolve("/api/cars/").view_name == "api:car-list"


@pytest.mark.django_db
def test_car_detail(api_rf: APIRequestFactory, user: User, car: Car):
    view = CarViewSet.as_view({"get": "retrieve"})

    request = api_rf.get(f"cars/{car.pk}")
    force_authenticate(request, user=user)
    response = view(request, pk=car.pk)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == CarSerializer(car).data


@pytest.mark.django_db
def test_rate_list():
    assert reverse("api:rate-list") == "/api/rate/"
    assert resolve("/api/rate/").view_name == "api:rate-list"


@pytest.mark.django_db
def test_rate_detail(api_rf: APIRequestFactory, user: User, car: Car, rate: Rating):
    view = RateViewSet.as_view({"get": "retrieve"})

    request = api_rf.get(f"rate/{rate.pk}")
    force_authenticate(request, user=user)
    response = view(request, pk=rate.pk)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == RatingSerializer(rate).data


@pytest.mark.django_db
def test_popular_list():
    assert reverse("api:popular-list") == "/api/popular/"
    assert resolve("/api/popular/").view_name == "api:popular-list"
