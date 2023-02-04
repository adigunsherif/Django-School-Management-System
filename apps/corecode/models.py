from django.urls import reverse
from django.utils import timezone
from django.db import models

#from apps.employees.models import Employee

# Create your models here.


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class PermitDocCategory(models.Model):
    """DocumentCategory"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Citizenship(models.Model):
    """Citizenship"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name

class AcademicSession(models.Model):
    """Academic Session"""

    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    """Academic Term"""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Subject"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name

class DocumentType(models.Model):
    """DocumentType"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Document(models.Model):
    STATUS_CHOICES = [("active", "Действующий"), ("inactive", "Архив")]

    #GENDER_CHOICES = [("male", "Муж"), ("female", "Жен")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name="Статус"
    )

    # employee = models.ForeignKey(
    #     Employee, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Сотрудник"
    # )

    doc_type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Тип документа"
    )

    serial = models.CharField(max_length=200, unique=True, verbose_name="Серия")
    number = models.CharField(max_length=200, verbose_name="Номер №")

    date_of_issue = models.DateField(default=timezone.now, verbose_name="Дата выдачи, С")
    date_of_expiry = models.DateField(default=timezone.now, verbose_name="Дата окончание, ДО")

    issued_authority = models.CharField(max_length=200, verbose_name="Кем выдан")

    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Гражданство"
    )

    address = models.TextField(blank=True, verbose_name="Адрес в РФ")
    others = models.TextField(blank=True, verbose_name="Другие")
    scanned_doc = models.FileField(blank=True, upload_to="documents/uploads/", verbose_name="Загрузить файл")

    class Meta:
        ordering = ["current_status"]
#        ordering = ["employee", "current_status"]
    def __str__(self):
        #return "{} {} {} {}".format(self.employee, self.current_status)
        return "{} {} {} {}".format(self.current_status)

    def get_absolute_url(self):
        return reverse("document-detail", kwargs={"pk": self.pk})


