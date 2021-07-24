from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


class ParentForm(ModelForm):
    class Meta:
        model = ParentMore
        fields = "__all__"

