
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.views.decorators.http import require_POST

@require_POST
def complete(request, id):
    task = get_object_or_404(Task, id=id)
    task.status = not task.status
    task.save()
    return redirect('list')

@require_POST
def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('list')

@require_POST
def add(request):
    task = Task()
    task.title = request.POST['title']
    task.save()

    return redirect('list')

def list(request):
    tasks = Task.objects.all()
    
    return render(request, 'list.html', {'tasks': tasks})
