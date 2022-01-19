from django.shortcuts import render
from .models import Todo


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'all': all})


def say_hello(request):
    admin_name = {'name': 'majid', 'last_name': 'nabilo'}
    return render(request, 'hello.html', context=admin_name)
