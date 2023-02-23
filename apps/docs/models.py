from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett

from apps.corecode.models import Citizenship, DocumentType
from apps.employees.models import Employee

# Create your models here.

class Doc(models.Model):
    STATUS_CHOICES = [("active", "Действующий"), ("inactive", "Архив")]

    #GENDER_CHOICES = [("male", "Муж"), ("female", "Жен")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name="Статус"
    )

    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Сотрудник"
    )

    doc_type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Тип документа"
    )

    serial = models.CharField(max_length=200, verbose_name="Серия") # unique=True, 
    number = models.CharField(max_length=200, verbose_name="Номер №")

    date_of_issue = models.DateField(default=timezone.now,  verbose_name="Дата выдачи")
    date_of_preparing = models.DateField(default=timezone.now, verbose_name="Начать оформить до")
    date_of_expiry = models.DateField(default=timezone.now, verbose_name="Действует до")

    issued_authority = models.CharField(max_length=200, verbose_name="Кем выдан")

    address = models.TextField(blank=True, verbose_name="Адрес в РФ")
    others = models.TextField(blank=True, verbose_name="Другие")
    scanned_doc = models.FileField(blank=True, upload_to="docs/uploads/", verbose_name="Загрузить файл")

    class Meta:
        ordering = ["current_status"]

    def __str__(self):
        return "{} - {}".format(self.doc_type, self.employee)

    def get_absolute_url(self):
        return reverse("doc-detail", kwargs={"pk": self.pk})

class DocBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="docs/bulkupload/")
