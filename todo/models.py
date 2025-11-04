from django.db import models
from django.forms import CharField

class Task(models.Model):
    name = models.CharField(max_length=200, blank=False)
    status = models.BooleanField(default=False)
    date = models.DateField()
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
            return self.name
    