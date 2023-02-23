from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett

from apps.corecode.models import PermitDocCategory, Citizenship


class Employee(models.Model):
    STATUS_CHOICES = [("active", "Работает"), ("inactive", "Уволенный")]

    GENDER_CHOICES = [("male", "Муж"), ("female", "Жен")]

    #STAFF_CHOICES = [("WhiteCollar", "Белый воротник"), ("BlueCollar", "Синий воротник")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name="Статус"
    )
    personnel_number = models.CharField(max_length=200, unique=True, verbose_name="Табельный номер")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    firstname = models.CharField(max_length=200, verbose_name="Имя")
    other_name = models.CharField(max_length=200, blank=True, verbose_name="Отчество")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", verbose_name="Пол")
    date_of_birth = models.DateField(default=timezone.now, verbose_name="Дата рождения")
    position = models.CharField(max_length=200, verbose_name="Должность")
    """ current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    ) """
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Гражданство"
    )

    current_doc_category = models.ForeignKey(
        PermitDocCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория документа"
    )
    date_of_employment = models.DateField(default=timezone.now, verbose_name="Дата приема")

    date_of_dismissal = models.DateField(verbose_name="Дата увольнение")

    tin_number = models.CharField(max_length=200, blank=True, verbose_name="ИНН")

    snils_number = models.CharField(max_length=200, blank=True, verbose_name="СНИЛС")

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True, verbose_name="Тел номер"
    )

    address = models.TextField(blank=True, verbose_name="Адрес в РФ")
    others = models.TextField(blank=True, verbose_name="Другие")
    photo = models.ImageField(blank=True, upload_to="employees/photos/", verbose_name="Фото")

    class Meta:
        ordering = ["personnel_number", "surname", "firstname", "other_name"]

    def __str__(self):
        #return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"
        return "{} {} {} ({})".format(self.surname, self.firstname, self.other_name, self.personnel_number)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})


class EmployeeBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="employees/bulkupload/")
