from django.urls import path
from . import views

urlpatterns = [
    path('conatactus/', views.say_contactus)
]
