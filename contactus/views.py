from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_contactus(request):
    return HttpResponse('contact us')
