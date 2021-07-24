from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from users.models import User
from users.forms import ParentForm


# Create your views here.
def ParentSignUpView(request):
    form = ParentForm()
    return  render(request,'Parent_Form.html', {"form": form})



