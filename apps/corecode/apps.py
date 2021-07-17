from django.apps import AppConfig


class CorecodeConfig(AppConfig):
    name = "apps.corecode"

    def ready(self):
        import apps.corecode.signals
