from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomTeachers(AbstractUser):
    ''
    GENDER = [
      ('male', 'Male'),
      ('female', 'Female')  ]
    staff_id = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=50)
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
    Email = models.EmailField(max_length=30)
    Department = models.CharField(max_length=15)
    Profile = models.TextField(blank=True)

    USERNAME_FIELD = 'staff_id'
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
