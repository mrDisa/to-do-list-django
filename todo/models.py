import uuid
from django.db import models
from django.forms import CharField

class Task(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=200, blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
            return self.title
    
    