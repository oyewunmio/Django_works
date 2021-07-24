from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.fields import proxy
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
from classes.models import Classes


# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        now = timezone.now()
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    #email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, null=True, blank=True,unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    #EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Types(models.TextChoices):
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        PARENT = "PARENT", "Parent"

    type = models.CharField(
        _('Type'), max_length=50, choices=Types.choices)

    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    
    """def get_absolute_url(self):
        return reverse("users:detail", kwargs={"": self.username})"""

    objects = UserManager()

"""class User(AbstractUser):
    class Types(models.TextChoices):
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        PARENT = "PARENT", "Parent"

    type = models.CharField(
        _('Type'), max_length=50, choices=Types.choices)

    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    
    \"""def get_absolute_url(self):
        return reverse("users:detail", kwargs={"": self.username})\"""
"""    
    
class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

class ParentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PARENT)

class Teacher(User): 
    base_type = User.Types.TEACHER
    objects = TeacherManager()

    @property
    def more(self):
        return self.teachermore
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.TEACHER
            
        return super().save(*args, **kwargs)
class TeacherMore(models.Model):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    Staff_id = models.CharField(max_length=50)
    Phone_number = PhoneField(blank=True, help_text='Contact phone number')
    Bio = models.TextField(blank=True)
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.Staff_id}'

    #subjects, class, profilepic

class Student(User):
    base_type = User.Types.STUDENT
    objects = StudentManager()

    @property
    def more(self):
        return self.studentmore
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)
class StudentMore(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    Staff_id = models.CharField(max_length=50)
    Phone_number = PhoneField(blank=True, help_text='Contact phone number')
    Bio = models.TextField(blank=True)
    #Class = models.ForeignKey(Classes, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f'{self.user} {self.Staff_id}'


class Parent(User):
    base_type = User.Types.PARENT
    objects = ParentManager()

    @property
    def more(self):
        return self.parentmore
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PARENT
        return super().save(*args, **kwargs)
class ParentMore(models.Model):
    Child = models.OneToOneField(Student, on_delete=models.CASCADE,default=False)
    Parent_id = models.CharField(max_length=50)
    Phone_number = PhoneField(blank=True, help_text='Contact phone number')
    Bio = models.TextField(blank=True)