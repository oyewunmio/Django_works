from django.db import models
from users.models import TeacherMore as Teacher

# Create your models here.
class Subjects(models.Model):
    Subjects_name = models.CharField(max_length=20)
    Subject_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.Subjects_name} {self.Subject_teacher}'
