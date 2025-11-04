
from django.shortcuts import render
from .models import Task

def delete():
    pass

def list(request):
    tasks = Task.objects.all()

    return render(request, 'list.html',
                  {'tasks': tasks})
