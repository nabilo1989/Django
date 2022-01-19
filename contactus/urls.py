from django.urls import path
from . import views

urlpatterns = [
    path('conatctus/', views.say_contactus)
]
