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
        fields = ['title', 'description', 'due_date', 'completed',]
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'edited': forms.HiddenInput()
        }

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        'todo',
        'done'
    ]

    # status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    search_query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}))
