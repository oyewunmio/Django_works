from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from users.models import *


# Create your views here.
def sthome(request):
    try:
        if request.user.is_authenticated and User.objects.get(username=request.user).type == 'STUDENT':
            StudentDetails = StudentMore.objects.get(user=User.objects.get(username=request.user))
            return render(request,'student_dashboard.html', {'More': StudentDetails})
        elif request.user.is_authenticated and User.objects.get(username=request.user).type == 'TEACHER':
            TeacherDetails = TeacherMore.objects.get(user=User.objects.get(username=request.user))
            return render(request,'teacher_dashboard.html', {'More': TeacherDetails})
        else:
            return redirect('login')
    except Exception:
        #messages.warning(request, "Warning: This is the sample warning Flash message.")
        return redirect('login')


