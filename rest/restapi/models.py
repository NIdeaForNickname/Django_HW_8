from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    deadline = models.DateTimeField()
