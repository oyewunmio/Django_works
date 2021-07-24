from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
import os
from classes.models import School_class


# Create your models here
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teachers(models.Model):
    GENDER = [
      ('male', 'Male'),
      ('female', 'Female')]
    picture =  models.ImageField(upload_to=os.path.join('BASE','passports'),blank=True)
    surname = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    Staff_id = models.CharField(max_length=100)
    mobile_num_regex    = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    mobile_number       = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
    gender              = models.CharField(max_length=10, choices=GENDER, default='male')
    bio =  models.TextField(blank=True)
    Class = models.ForeignKey(to=School_class, on_delete=models.SET_NULL, blank=True, null=True)


class Students(models.Model):
    GENDER = [
      ('male', 'Male'),
      ('female', 'Female')]
    picture =  models.ImageField(upload_to=os.path.join('BASE','passports'), blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    surname = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    other_name          = models.CharField(max_length=200, blank=True)
    gender              = models.CharField(max_length=10, choices=GENDER, default='male')
    date_of_birth       = models.DateField(default=timezone.now)
    date_of_admission   = models.DateField(default=timezone.now)
    Class = models.ForeignKey(to=School_class, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f'{self.surname} {self.first_name} {self.other_name} {self.Class}'




