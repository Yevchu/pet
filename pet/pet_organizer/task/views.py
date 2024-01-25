from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q

from .models import Task
from .forms import TaskForm, UpdateTaskForm, TaskFilterForm

# Create your views here.

def main(request):
    return render(request, 'task/base.html')

def search_by_name(tasks, search_query):
    if search_query:
        return tasks.filter(title__icontains=search_query)
    return tasks

def search_by_status(tasks, status_filter):
    if status_filter:
        if status_filter == 'todo':
            return tasks.filter(completed=False)
        elif status_filter == 'done':
            return tasks.filter(completed=True)
    return tasks

def task_list(request):    
    search_query = request.GET.get('search_query')
    status_filter = request.GET.get('status_filter')

    tasks = Task.objects.all()
    tasks = search_by_name(tasks, search_query)
    tasks = search_by_status(tasks, status_filter)

    task_done = tasks.filter(completed=True)
    task_todo = tasks.filter(completed=False)
    return render(request, 'task/task_list.html', {'task_done': task_done, 'task_todo': task_todo, 'search_query': search_query, 'status_filter': status_filter})

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
            messages.error(request, "Invalid data. Please fix the errors below.")
    else:
        form = UpdateTaskForm(instance=task)
    
    return render(request, 'task/update_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect(to='task_list')
    
    return render(request, 'task/delete_task.html', {'task': task})

