from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/tasks_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfuly')
            return redirect(to='task_list')
        else: 
            messages.error(request, 'Some data is invalid.')
    else: 
        form = TaskForm()
    
    return render(request, 'task/create_task.html', {'form': form})

def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render (request, 'task/view_task.html', {'task': task})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.instance.edited = timezone.now()
            form.save()
            return redirect(to='task_list')
        else:
            messages.error(request, "Invalid data.")
    else:
        form = UpdateTaskForm(instance=task)
    
    return render(request, 'task/update_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect(to='task_list')
    
    return render(request, 'task/delete_task.html', {'task': task})
