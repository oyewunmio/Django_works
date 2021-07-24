from django.urls import path, include
from .views import ParentSignUpView
from django.views.generic import CreateView

urlpatterns = [
    path('createParent/',ParentSignUpView, name='parent_register'),
    #path('createStudent/', StudentForm,name = 'student_register'),
    #path(route, view, name=str)
]
