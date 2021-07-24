from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('login/',loginView, name='login'),
    path('logout/',user_logout,name='logout'),
]