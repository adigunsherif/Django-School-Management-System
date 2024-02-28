from django.urls import reverse
from django.utils import timezone
from django.db import models

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

    name = models.CharField(max_length=100)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Gen_DT_Country(models.Model):
    """Gen_DT_Country"""

    CountryCode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, verbose_name="CountryEN")
    CountryRU = models.CharField(max_length=100)
    CountryTR = models.CharField(max_length=100)
    AlphaCode2 = models.CharField(max_length=10, default="000", verbose_name="AlphaCode(2)")
    AlphaCode3 = models.CharField(max_length=10, verbose_name="AlphaCode(3)")
    CountriesForRF = models.BooleanField(default=False)
    LocalEEC = models.BooleanField(default=False, verbose_name="Local/ EEC")
    RvpVnj = models.BooleanField(default=False, verbose_name="RVP/ VNJ")
    Visa = models.BooleanField(default=False)
    VKS = models.BooleanField(default=False)
    Patent = models.BooleanField(default=False)

    class Meta:
        #verbose_name =CountryEN "Наименование"
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

