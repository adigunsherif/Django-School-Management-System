from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = "apps.students"

    def ready(self):
        import apps.students.signals
