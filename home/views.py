from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def say_hello(request):
    admin_name = {'name': 'majid', 'last_name': 'nabilo'}
    return render(request, 'hello.html', context=admin_name)
