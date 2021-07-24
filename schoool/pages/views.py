from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as dj_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.models import *
from django.urls import reverse_lazy
#import .models for the subject and classes views
from django.views.generic import TemplateView, CreateView
from users.forms import ParentForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(request, username=uname, password=upass)
            print(user, uname, upass)

            if user is not None:
                dj_login(request, user)
                type_obj = User.objects.get(username=user)
                if user.is_authenticated and type_obj.type =='STUDENT':
                    try:
                        details_checker = StudentMore.objects.get(user=user)
                    except Exception:
                        messages.error(request, 'Student Not Registered..Meet Admin')
                    return redirect('shome') #Go to teacher home
                elif user.is_authenticated and type_obj.type == 'TEACHER':
                    try:
                        details_checker = TeacherMore.objects.get(user=user)
                    except Exception:
                        messages.error(request, 'Teacher not Registered..Meet Admin')
                    return redirect('shome') #Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            messages.error(request, 'Wrong credentials')
            #return redirect('home')           
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login/')

