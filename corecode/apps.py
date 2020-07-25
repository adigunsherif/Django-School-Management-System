from django.apps import AppConfig


class CorecodeConfig(AppConfig):
    name = 'corecode'

    def ready(self):
        import corecode.signals
