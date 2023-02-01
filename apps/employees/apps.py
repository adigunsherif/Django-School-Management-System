from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = "apps.employees"

    def ready(self):
        import apps.employees.signals