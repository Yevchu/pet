from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=225, verbose_name = 'Task name')
    description = models.TextField(blank=True, null=True, verbose_name = 'Task description')
    due_date = models.DateTimeField(verbose_name = 'Deadline')
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False, verbose_name = 'Completed')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
    