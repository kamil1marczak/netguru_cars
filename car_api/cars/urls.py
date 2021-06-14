from django.urls import path, include
from car_api.cars.api.views import CarViewSet, RateViewSet, PopularCarViewSet

# from netguru_project.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
# router.register(r'car', CarViewSet, basename='car')
# router.register(r'rate', RateViewSet, basename='rate')
# router.register(r'popular', PopularCarViewSet, basename='popular')

app_name = "cars"
urlpatterns = [
    # path('v1/', include(router.urls)),
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
