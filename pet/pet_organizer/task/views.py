from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
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
