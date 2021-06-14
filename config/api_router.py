from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from car_api.users.api.views import UserViewSet
from car_api.cars.api.views import CarViewSet, RateViewSet, PopularCarViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(r'car', CarViewSet, basename='car')
router.register(r'rate', RateViewSet, basename='rate')
router.register(r'popular', PopularCarViewSet, basename='popular')


app_name = "api"
urlpatterns = router.urls
