from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('Signup/', SignUpView.as_view(),name='signup'),
]