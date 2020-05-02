from django.db import models

from corecode.models import AcademicSession, AcademicTerm, StudentClass, Subject
from students.models import Student

# Create your models here.
class Result(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
  term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
  current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  test_score = models.IntegerField(default=0)
  exam_score = models.IntegerField(default=0)

  def __str__(self):
    return f'{self.student} {self.session} {self.term} {self.subject}'

  def total_score(self):
    return self.test_score + self.exam_score
