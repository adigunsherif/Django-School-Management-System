from django.db import models
from django.utils import timezone
from django.urls import reverse

class Staff(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  current_status = models.CharField(
      max_length=10, choices=STATUS, default='active')
  surname = models.CharField(max_length=200)
  firstname = models.CharField(max_length=200)
  other_name = models.CharField(max_length=200, blank=True)
  gender = models.CharField(max_length=10, choices=GENDER, default='male')
  date_of_birth = models.DateField(default=timezone.now)
  date_of_admission = models.DateField(default=timezone.now)
  mobile_number = models.CharField(max_length=15, blank=True)
  address = models.TextField(blank=True)
  others = models.TextField(blank=True)

  def __str__(self):
    return f'{self.surname} {self.firstname} {self.other_name}'

  def get_absolute_url(self):
    return reverse('staff-detail', kwargs={'pk': self.pk})
