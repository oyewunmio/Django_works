from django.shortcuts import render
from django.contrib.auth.views import LoginView    
from django.urls import reverse_lazy


# Create your views here.
class LoginPageView(LoginView):
    success_url = reverse_lazy('home')
    template_name = 'login.html'

