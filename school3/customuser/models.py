
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


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

    objects = UserManager()

    """def get_absolute_url(self):
        return "/users/%i/" % (self.pk)"""
    def get_username(self):
        return self.username


class user_type(models.Model):
     is_teach = models.BooleanField(default=False)
     is_student = models.BooleanField(default=False)
     user = models.OneToOneField(User, on_delete=models.CASCADE)

     def __str__(self):
         if self.is_student == True:
             return User.get_username(self.user) + " - is_student"
         else:
             return User.get_username(self.user) + " - is_teacher"
