from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CarsConfig(AppConfig):
    name = "car_api.cars"
    verbose_name = _("Cars")

    def ready(self):
        try:
            import car_api.cars.signals  # noqa F401
        except ImportError:
            pass
