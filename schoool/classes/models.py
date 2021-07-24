from django.db import models
#from users.models import Teacher

# Create your models here.
class Classes(models.Model):
    Classes_CHOICES = [
    ('SCIENCE', 'Science'),
    ('COMMERCIAL', 'Commercial'),
    ('ARTS', 'Arts'),
]
    Class_name = models.CharField(max_length=10, unique=True)
    Category = models.CharField(max_length=12, choices=Classes_CHOICES, null=True )
    #Teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    #Students = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Class_name} {self.Category}'