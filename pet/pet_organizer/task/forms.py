from django import forms
from .models import Task
from datetime import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
class UpdateTaskForm(TaskForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'edited']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'edited': forms.HiddenInput()
        }
