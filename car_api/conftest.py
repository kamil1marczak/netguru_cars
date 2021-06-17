import pytest
from pytest_django.lazy_django import skip_if_no_django

from car_api.users.models import User
from car_api.cars.models import Car, Rating
from car_api.users.tests.factories import UserFactory
from car_api.cars.tests.factories import CarFactory, RateFactory
from rest_framework.test import APIRequestFactory


@pytest.fixture()
def api_rf() -> APIRequestFactory:
    """
    APIRequestFactory instance
    """
    skip_if_no_django()

    return APIRequestFactory()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def car() -> Car:
    return CarFactory()


@pytest.fixture
def rate() -> Rating:
    return RateFactory()
