from django.shortcuts import render
from django.http import HttpResponse # new

# Create your views here.
'Views are python functions that receives an Http request object and returns an Http response object '

def home(request):
    return HttpResponse('Hello world')


