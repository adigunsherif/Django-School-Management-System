import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student, StudentBulkUpload

@receiver(post_save, sender=StudentBulkUpload)
def create_bulk_student(sender, created, instance, *args, **kwargs):
  if created:
    opened = StringIO(instance.csv_file.read().decode())
    reading = csv.DictReader(opened, delimiter=',')
    students = []
    for row in reading:
      reg = row['registration_number'] if 'registration_number' in row and row['registration_number'] else ''
      surname = row['surname'] if 'surname' in row and row['surname'] else ''
      firstname = row['firstname'] if 'firstname' in row and row['firstname'] else ''
      other_names = row['other_names'] if 'other_names' in row and row['other_names'] else ''
      gender = (row['gender']).lower(
      ) if 'gender' in row and row['gender'] else ''
      phone = row['parent_number'] if 'parent_number' in row and row['parent_number'] else ''
      address = row['address'] if 'address' in row and row['address'] else ''

      check = Student.objects.filter(registration_number=reg)
      if not check:
        students.append(
          Student(
              registration_number=reg,
              surname=surname,
              firstname=firstname,
              other_name=other_names,
              gender=gender,
              current_class=instance.current_class,
              parent_mobile_number=phone,
              address=address,
              current_status='active'
          )
        )

    Student.objects.bulk_create(students)
    instance.csv_file.close()
    instance.delete()

@receiver(post_delete, sender=StudentBulkUpload)
def delete_file(sender, instance, *args, **kwargs):
  if instance.csv_file:
    if os.path.isfile(instance.csv_file.path):
        os.remove(instance.csv_file.path)

