from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.corecode.models import StudentClass


class Student(models.Model):
    STATUS_CHOICES = [("active", "Работает"), ("inactive", "Уволенный")]

    GENDER_CHOICES = [("male", "Муж"), ("female", "Жен")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name="Статус"
    )
    registration_number = models.CharField(max_length=200, unique=True, verbose_name="Табельный номер")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    firstname = models.CharField(max_length=200, verbose_name="Имя")
    other_name = models.CharField(max_length=200, blank=True, verbose_name="Отчество")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", verbose_name="Пол")
    date_of_birth = models.DateField(default=timezone.now, verbose_name="Дата рождения")
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_of_admission = models.DateField(default=timezone.now, verbose_name="Дата приема")

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True, verbose_name="Тел номер"
    )

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/", verbose_name="Паспорт")

    class Meta:
        ordering = ["surname", "firstname", "other_name"]

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
