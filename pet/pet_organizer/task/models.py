from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=225, verbose_name = 'Task name')
    description = models.TextField(blank=True, null=True, verbose_name = 'Task description')
    due_date = models.DateTimeField(verbose_name = 'Deadline')
    completed = models.BooleanField(default=False, verbose_name = 'Completed')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
    