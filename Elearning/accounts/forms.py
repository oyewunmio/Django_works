from Elearning.classes.models import Classes
from django.contrib.auth.forms import  UserCreationForm
from django.forms.widgets import NumberInput
from django.db import transaction
from .models import Teachers, User, Student
from classes.models import Classes


GENDER = [
      ('male', 'Male'),
      ('female', 'Female')]


class TeachersSignUpForm(UserCreationForm):
    Surname = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    Staff_id = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[GENDER], required=True)
    phone_no = forms.CharField(required=True)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    Class = forms.ModelMultipleChoiceField(
        queryset=Classes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class meta(UserCreationForm.Meta):
        model = User
        fields = ()
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.surname = self.cleaned_data.get('surname')
        user.first_name = self.cleaned_data.get('first_name')
        user.save()
        teachers = Teachers.objects.create(user=user)
        staff_id = self.cleaned_data.get('Staff_id')
        phone_no = self.cleaned_data.get('phone_no')
        return user



class StudentsSignUpForm(UserCreationForm):
    Surname = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    date_of_admission = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    bio = forms.CharField(required=False)

    class meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.surname = self.cleaned_data.get('surname')
        user.first_name = self.cleaned_data.get('first_name')
        user.save()
        teachers = Teachers.objects.create(user=user)
        staff_id = self.cleaned_data.get('Staff_id')
        phone_no = self.cleaned_data.get('phone_no')
        return user